# File: claims.models.py
# Description: execute sql query then return value to views
# Author                                Date                                         Change Description
# NLQHuy, HMThu                         2020/04/08                                   Create new
# NLQHuy                                2020/05/09                                   Fix bug claim search, load combobox operator

import datetime
import re

from utils import mysql_connection
from utils import response_json
# from ..commons import mod_const
from . import contants


def btn_get_data_claim_group():
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        claim_group_cbb = []
        claim_group_default = {
            'claim_group_id': 0,
            'name': "",
        }
        claim_group_cbb.append(claim_group_default)

        sql_claim_group = "SELECT claim_group_id, name FROM claim_groups WHERE del_flg = 0 ORDER BY sort ASC"

        cursor.execute(sql_claim_group)
        data_claimgroup = cursor.fetchall()
        if cursor.rowcount > 0:
            for item in data_claimgroup:
                temp_list = {
                    'claim_group_id': item['claim_group_id'],
                    'name': item['name'],
                }
                claim_group_cbb.append(temp_list)

        response['code'] = 0
        response['data_claimgroup'] = claim_group_cbb

    except Exception as e:
        print('claims.models -> btn_get_data_claim_group -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()
    return response


def btn_get_data_operator():
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        operator_cbb = []
        operator_cbb_default = {
            'user_id': 0,
            'username': "",
        }
        operator_cbb.append(operator_cbb_default)

        sql_claim_user = "SELECT user_id, username FROM users WHERE del_flg = 0 ORDER BY sort ASC"

        cursor.execute(sql_claim_user)
        data_claim_user = cursor.fetchall()

        if cursor.rowcount > 0:
            for item in data_claim_user:
                temp_list = {
                    'user_id': item['user_id'],
                    'username': item['username'],
                }
                operator_cbb.append(temp_list)

        response['code'] = 0
        response['data_claim_user'] = operator_cbb

    except Exception as e:
        print('claims.models -> btn_get_data_operator -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()
    return response


# ----btn_claim_search_click
def btn_claim_search_click(claim_search_arg):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)

    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()
        response['table_total_row'] = 0
        str_where = get_claim_search_where(claim_search_arg)

        if claim_search_arg['btn_flag_click']:
            sql_count_row = """SELECT count(*) as total
                FROM 
                    claims 
                LEFT JOIN 
                    users 
                ON 
                    claims.user_id = users.user_id
                LEFT JOIN
                    claim_groups cg
                ON
                    claims.claim_group_id = cg.claim_group_id"""

            if str(str_where) != "":
                sql_count_row += " WHERE"
                sql_count_row += str(str_where).replace('"', "'")

            cursor.execute(sql_count_row)
            data_search_count_all = cursor.fetchone()

            response['table_total_row'] = data_search_count_all['total']
            if claim_search_arg['limit_cnt'] != "" and claim_search_arg['limit_cnt'] is not None:
                if int(claim_search_arg['limit_cnt']) < int(data_search_count_all['total']):
                    response['table_total_row'] = int(claim_search_arg['limit_cnt'])
                else:
                    response['table_total_row'] = data_search_count_all['total']
            else:
                response['table_total_row'] = data_search_count_all['total']

        sql_search = """
            SELECT
                claims.id, 
                claims.claim_group_id,
                DATE_FORMAT(claims.created,'%y/%m/%d %H:%i') AS created_hour, 
                DATE_FORMAT(claims.created,'%y/%m/%d') AS created, 
                cg.name AS cg_name, 
                claims.name, 
                claims.tel,
                CASE WHEN users.username IS NULL THEN 'システム' ELSE users.username END username, 
                biko
            FROM 
                claims 
            LEFT JOIN 
                users 
            ON 
                claims.user_id = users.user_id
            LEFT JOIN
                claim_groups cg
            ON
                claims.claim_group_id = cg.claim_group_id"""

        if str(str_where) != "":
            sql_search += " WHERE"
            sql_search += str(str_where).replace('"', "'")
        sql_search += " ORDER BY created DESC"
        sql_search += " LIMIT " + str(claim_search_arg['row_current_page']) + ", " + str(claim_search_arg['row_per_page'])

        cursor.execute(sql_search)
        data_search_table = cursor.fetchall()

        response['code'] = 0
        response['data_search_table'] = data_search_table

    except Exception as e:
        print('claims.models -> btn_claim_search_click -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()
    return response


def get_claim_search_where(claim_search_arg):
    str_where = ""

    flag_str = False
    if int(claim_search_arg['claim_create_date_check']):
        str_where += f""" claims.created >= STR_TO_DATE("{mod_const.get_dtp_mysql_format(claim_search_arg['claim_create_date_start'])}", '%Y-%m-%d %H:%i:%s') """
        str_where += " AND "
        str_where += f""" claims.created <= STR_TO_DATE("{mod_const.get_dtp_mysql_format(claim_search_arg['claim_create_date_end'], True)}", '%Y-%m-%d %H:%i:%s') """
        flag_str = True

    if claim_search_arg['claim_group_id'] > 0:
        if flag_str:
            str_where += " AND "

        str_where += f""" claims.claim_group_id = "{claim_search_arg['claim_group_id']}" """
        flag_str = True

    if claim_search_arg['user_id'] > 0:
        if flag_str:
            str_where += " AND "

        str_where += f""" claims.user_id = "{claim_search_arg['user_id']}" """
        flag_str = True

    if str(claim_search_arg['name']).rstrip() != "":
        if flag_str:
            str_where += " AND "

        str_where += f""" claims.name LIKE {mod_const.sql_null_or_str(claim_search_arg['name'], 1)} """
        flag_str = True

    if claim_search_arg['tel_for_find'] != "":
        if flag_str:
            str_where += " AND "

        claim_search_arg['tel_for_find'] = str(claim_search_arg['tel_for_find']).strip()

        if " " in claim_search_arg['tel_for_find']:
            claim_search_arg['tel_for_find'] = re.sub(r"[^0-9 ]", "", claim_search_arg['tel_for_find'])
            tels = str(claim_search_arg['tel_for_find']).replace(" ", "','")
            str_where += f" claims.tel_for_find IN ('{tels}') "
        else:
            str_where += f""" claims.tel_for_find LIKE {mod_const.sql_null_or_str(mod_const.get_number_only(claim_search_arg['tel_for_find']), 1)} """

        flag_str = True

    if str(claim_search_arg['biko']).rstrip() != "":
        if flag_str:
            str_where += " AND "

        str_where += f""" claims.biko LIKE {mod_const.sql_null_or_str(claim_search_arg['biko'], 1)} """

    if str(claim_search_arg['cg_name_kensaku']).rstrip() != "":
        if flag_str:
            str_where += " AND "

        str_where += f""" cg.name LIKE {mod_const.sql_null_or_str(claim_search_arg['cg_name_kensaku'], 1)} """
        flag_str = True

    if str(claim_search_arg['name_kensaku']).rstrip() != "":
        if flag_str:
            str_where += " OR "

        str_where += f""" users.username LIKE {mod_const.sql_null_or_str(claim_search_arg['name_kensaku'], 1)} """
        flag_str = True

    if str(claim_search_arg['name_kensaku']).rstrip() != "":
        if flag_str:
            str_where += " OR "

        str_where += f""" claims.name LIKE {mod_const.sql_null_or_str(claim_search_arg['name_kensaku'], 1)} """
        flag_str = True

    if str(claim_search_arg['tel_kensaku']).rstrip() != "":
        if flag_str:
            str_where += " OR "

        str_where += f""" claims.tel_for_find LIKE {mod_const.sql_null_or_str(claim_search_arg['tel_kensaku'], 1)} """

    return str_where


# ----btn_claim_get_data_selected
def btn_claim_get_data_selected(id_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    response['data_claim_obj'] = {}
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql_claim_id = """SELECT claims.id, 
                                DATE_FORMAT(claims.created,'%%y/%%m/%%d') AS created, 
                                cg.name AS cg_name, 
                                claims.name, claims.tel, 
                                biko, 
                                users.username
                            FROM claims 
                            LEFT JOIN users 
                            ON claims.user_id = users.user_id 
                            LEFT JOIN claim_groups cg 
                            ON claims.claim_group_id = cg.claim_group_id WHERE id = %s"""

        cursor.execute(sql_claim_id, (id_input))
        data_claim_obj = cursor.fetchone()

        response['code'] = 0
        response['data_claim_obj'] = data_claim_obj

    except Exception as e:
        print('claims.models -> btn_claim_get_data_selected -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


# ----btn_claim_add_click
def btn_claim_add_click(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql_duplicate = "SELECT COUNT(tel) AS duplicate FROM claims "
        sql_duplicate += f"""WHERE tel_for_find = "{mod_const.get_number_only(obj_data_input['tel'])}" """
        sql_duplicate += f"""AND claim_group_id = "{obj_data_input['claim_group_id']}" """

        cursor.execute(sql_duplicate)
        duplicate_output_check = cursor.fetchone()

        if duplicate_output_check['duplicate'] > 0:
            response = contants.get_response_claim_add("ER09.3-04")
        else:
            sql_add = """INSERT INTO claims 
                (claim_group_id, 
                name, 
                tel, 
                tel_for_find, 
                user_id, 
                biko, 
                created, 
                modified) 
            VALUES (%s, %s, %s, %s, 0, %s, NOW(), NOW())"""
            cursor.execute(sql_add,
                           (obj_data_input['claim_group_id'],
                            obj_data_input['name'],
                            obj_data_input['tel'],
                            obj_data_input['tel'],
                            obj_data_input['biko']
                            )
                           )
            flag_result_add = cursor.rowcount

            print("flag_insert_add", flag_result_add)
            if flag_result_add > 0:
                connection.commit()
                response['code'] = 0
            else:
                connection.rollback()
                response['code'] = ""

            response['code'] = 0
    except Exception as e:
        response = contants.get_response_claim_add("ER09.3-03")
        if connection is not None:
            connection.rollback()
        print('claims.models -> btn_claim_add_click -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


# ----btn_claim_edit_click
def btn_claim_edit_click(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    # glbIntOperatorId = 0
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql_duplicate = "SELECT COUNT(tel) AS duplicate FROM claims "
        sql_duplicate += f"""WHERE tel_for_find = "{mod_const.get_number_only(obj_data_input['tel'])}" """
        sql_duplicate += f"""AND claim_group_id = "{obj_data_input['claim_group_id']}" """
        if obj_data_input['id'] is not None and obj_data_input['id'] != '':
            if obj_data_input['id'] > 0:
                sql_duplicate += f""" AND NOT id = "{obj_data_input['id']}" """

        cursor.execute(sql_duplicate)
        duplicate_output_check = cursor.fetchone()

        if duplicate_output_check['duplicate'] > 0:
            response = contants.get_response_claim_edit("ER09.3-04")
        else:
            sql_edit = """
            UPDATE claims 
            SET
                name = %s,
                tel =  %s,
                tel_for_find = %s,
                user_id = 0,
                biko = %s,
                modified = Now()
            WHERE id = %s"""

            cursor.execute(sql_edit, (
                obj_data_input['name'],
                obj_data_input['tel'],
                obj_data_input['tel'],
                obj_data_input['biko'],
                obj_data_input['id']
            ))

            flag_result_edit = cursor.rowcount
            if flag_result_edit > 0:
                connection.commit()
                response['code'] = 0
            else:
                connection.rollback()
                response['code'] = 1
    except Exception as e:
        response = contants.get_response_claim_edit("ER09.3-03")
        if connection is not None:
            connection.rollback()
        print('claims.models -> btn_claim_edit_click -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


# ----btn_claim_del_click
def btn_claim_del_click(claim_group_id):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)

    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql = "START TRANSACTION;"
        cursor.execute(sql)

        id_list = []
        for item in claim_group_id:
            id_list.append(str(item['id']))

        where_tel = "','".join(id_list)
        del_sql = f"""DELETE FROM claims WHERE id IN ('{where_tel}') """
        cursor.execute(del_sql)
        flag_result_del = cursor.rowcount

        if flag_result_del > 0:
            sql = "COMMIT;"
            cursor.execute(sql)
            connection.commit()
            response['code'] = 0
        else:
            connection.rollback()
            response['code'] = ""
    except Exception as e:
        if connection is not None:
            connection.rollback()
        print('claims.models -> btn_claim_del_click -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
    return response


# -----btn_claim_group_add_click
def btn_claim_group_get_data_selected():
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()
        claim_group_list = []

        sql_get_data_claim_group = "SELECT * FROM claim_groups WHERE del_flg = 0 ORDER BY sort ASC"

        cursor.execute(sql_get_data_claim_group)

        data_claim_group = cursor.fetchall()
        if cursor.rowcount > 0:
            for item in data_claim_group:
                temp_list = {
                    'claim_group_id': item['claim_group_id'],
                    'name': item['name'],
                    'sort': item['sort'],
                }
                claim_group_list.append(temp_list)

        response['code'] = 0
        response['data_claim_group'] = claim_group_list

    except Exception as e:
        print('claims.models -> btn_claim_group_get_data_selected -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


# -----btn_claim_group_add_click
def btn_claim_group_add_click(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql_claim_group_add_get_sort = "SELECT CASE WHEN sort IS NULL THEN 0 ELSE sort END sort FROM claim_groups WHERE del_flg = 0 ORDER BY sort desc LIMIT 1"
        cursor.execute(sql_claim_group_add_get_sort)
        sort_next = cursor.fetchone()

        if sort_next is None:
            sort = 0
        else:
            sort = sort_next['sort']

        sql_operator_group_add = f"""INSERT INTO claim_groups(name, sort, del_flg, created, modified) VALUES ("{obj_data_input['name']}", {sort + 1}, 0, NOW(), NOW())"""

        cursor.execute(sql_operator_group_add)

        flag_result_claim_add = cursor.rowcount
        if flag_result_claim_add > 0:
            connection.commit()
            response['code'] = 0
        else:
            connection.rollback()
            response['code'] = ""

    except Exception as e:
        if connection is not None:
            connection.rollback()
        print('claims.models -> btn_claim_group_add_click -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


# -----btn_claim_group_edit_click
def btn_claim_group_edit_click(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql_claim_group_edit = "UPDATE claim_groups SET name = %s, modified = NOW() WHERE claim_group_id = %s"

        cursor.execute(sql_claim_group_edit, (obj_data_input['name'], obj_data_input['claim_group_id']))

        flag_result_claim_group_edit = cursor.rowcount
        if flag_result_claim_group_edit > 0:
            connection.commit()
            response['code'] = 0
        else:
            connection.rollback()
            response['code'] = 1

    except Exception as e:
        if connection is not None:
            connection.rollback()
        print('claims.models -> btn_claim_group_edit_click -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


# btn_claim_group_del_click
def btn_claim_group_del_click(claim_group_id):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql_claim_group_del = "UPDATE claim_groups SET del_flg = 1, modified = Now() WHERE claim_group_id = %s"
        cursor.execute(sql_claim_group_del, claim_group_id)

        flag_result_del = cursor.rowcount
        if flag_result_del > 0:
            connection.commit()
            response['code'] = 0
        else:
            connection.rollback()
            response['code'] = ""

        response['code'] = 0
    except Exception as e:
        print('claims.models -> btn_claim_group_del_click -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


# -----getClaimCount
def get_claim_count():
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        strWhere = ""
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql_get_claim_count = "SELECT COUNT(id) claim_cnt FROM claims"
        if strWhere != "":
            sql_get_claim_count += " WHERE" + strWhere

        cursor.execute(sql_get_claim_count)

        data_get_claim_count = cursor.fetchall()

        response['code'] = 0
        response['data_get_claim_count'] = data_get_claim_count

    except Exception as e:
        print('claims.models -> getClaimCount -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


# function: set_sort_down
# parameter: obj_data_input - json data type
# return: response - json data type
# description: sorting data when click up or down
def set_sort_up_down(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()
        sql_get_row_2 = ""
        if obj_data_input['flag'] == 'up':
            sql_get_row_2 = "SELECT claim_group_id, sort FROM claim_groups WHERE del_flg = 0 AND sort <= %s AND claim_group_id <> %s ORDER BY sort DESC LIMIT 1"
        elif obj_data_input['flag'] == 'down':
            sql_get_row_2 = "SELECT claim_group_id, sort FROM claim_groups WHERE del_flg = 0 AND sort >= %s AND claim_group_id <> %s ORDER BY sort ASC LIMIT 1"

        cursor.execute(sql_get_row_2, (obj_data_input['sort'], obj_data_input['claim_group_id']))
        if cursor.rowcount == 1:
            data_row_2 = cursor.fetchone()

            user_group_id_row_2 = data_row_2['claim_group_id']
            sort_row_2 = data_row_2['sort']

            sql_operator_update_row_1 = "UPDATE claim_groups SET sort = %s WHERE claim_group_id = %s"
            cursor.execute(sql_operator_update_row_1, (obj_data_input['sort'], user_group_id_row_2))
            flag_row_1 = cursor.rowcount

            sql_operator_update_row_2 = "UPDATE claim_groups SET sort = %s WHERE claim_group_id = %s"
            cursor.execute(sql_operator_update_row_2, (sort_row_2, obj_data_input['claim_group_id']))
            flag_row_2 = cursor.rowcount

            if flag_row_1 == 1 and flag_row_2 == 1:
                connection.commit()
                response['code'] = 0
            else:
                connection.rollback()
                response['code'] = 'ERR09.03-09'
        else:
            response['code'] = 'ERR09.03-09'
    except Exception as e:
        if connection is not None:
            connection.rollback()
        print('prospects.models -> set_sort_up_down -> ex: ', e)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
    return response


# function: get_selected_claim
# parameter: claim_id - int
# return: response - json data type
# description: get data of selected claim row
def get_selected_claim(claim_id):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        sql = "SELECT * FROM claim_groups WHERE claim_group_id = %s"
        cursor.execute(sql, claim_id)

        selected_result = cursor.fetchone()
        if cursor.rowcount > 0:
            response['selected_claim'] = selected_result
            response['code'] = 0
        else:
            response['code'] = ""
    except Exception as e:
        print('prospects.models -> set_sort_up_down -> ex: ', e)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
    return response


# function: import_csv_claim
# parameter: obj_input - json type
# return: response - json data type
# description: sql query import claim data
def import_csv_claim(claim_group_id, obj_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection()
        cursor = connection.cursor()

        claim_value_list = []
        count = 0

        sql = ""
        sql += "INSERT IGNORE INTO claims "
        sql += "("
        sql += "claim_group_id, "
        sql += "name, "
        sql += "tel, "
        sql += "tel_for_find, "
        sql += "biko, "
        sql += "created, "
        sql += "modified"
        sql += ") VALUES (%s, %s, %s ,%s, %s, %s, %s)"

        for item in obj_input:
            if mod_const.get_number_only(str(item['tel'])) == "":
                continue
            tel = mod_const.get_number_only(str(item['tel']))
            claim_value_list.append((
                str(claim_group_id),
                str(item['name']),
                tel,
                tel,
                item['biko'],
                str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            ))
            count += 1

        if count == 0:
            response['code'] = 'MSG09.04-01'
        else:
            cursor.executemany(sql, claim_value_list)
            check_row = cursor.rowcount

            connection.commit()
            if int(check_row) == 0:
                response['cnt'] = 0
            else:
                response['cnt'] = check_row
            response['code'] = 0
    except Exception as e:
        if connection is not None:
            connection.rollback()
        print('prospects.models -> import_csv_claim -> ex: ', e)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
    return response
