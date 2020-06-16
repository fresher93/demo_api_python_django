from utils import mysql_connection
from utils import response_json
from . import contants


def requesters_search(obj_data_input):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_search_exist = f"SELECT count(1) as cnt FROM requesters WHERE user_name={obj_data_input['user_name']}"

        cursor.execute(sql_search_exist)

        if cursor.rowcount > 0:
            response['code'] = 1

        elif cursor.rowcount == 0:
            sql_insert = f"INSERT INTO requesters(user_name, password, created_date, update_date) values(\"{obj_data_input['user_name']}\", \"{obj_data_input['password']}\", now(), now())"

            cursor.execute(sql_insert)
            connection.commit()

            response['code'] = 0

    except Exception as e:
        print('regist.models -> requesters_search -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response
