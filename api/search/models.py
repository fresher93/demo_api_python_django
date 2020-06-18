from utils import mysql_connection
from utils import response_json


def requesters_search(obj_input_data):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    obj_output_data = []
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()
        sql_search = f"SELECT * FROM requests WHERE requesters_id={obj_input_data['user_id']}"

        if obj_input_data['search_type'] == 0:
            return response

        else:
            if obj_input_data['search_type'] == 1:
                sql_search += f" AND request_date=\"{obj_input_data['search_data']}\" "

            elif obj_input_data['search_type'] == 2:
                sql_search += f" AND device=\"{obj_input_data['search_data']}\" "

            elif obj_input_data['search_type'] == 3:
                sql_search += f" AND name=\"{obj_input_data['search_data']}\" "
            
            cursor.execute(sql_search)

            list_request = cursor.fetchall() if cursor.rowcount > 0 else []

        response['code'] = 0
        response['list_request'] = list_request

    except Exception as e:
        print('search.models -> requesters_search -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


def technicals_search(obj_input_data):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    obj_output_data = []
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()
        sql_search = f"SELECT * FROM requests WHERE technicals_id={obj_input_data['user_id']}"

        if obj_input_data['search_type'] == 0:
            return response

        else:
            if obj_input_data['search_type'] == 1:
                sql_search += f" AND request_date=\"{obj_input_data['search_data']}\" "

            elif obj_input_data['search_type'] == 2:
                sql_search += f" AND device=\"{obj_input_data['search_data']}\" "

            elif obj_input_data['search_type'] == 3:
                sql_search += f" AND name=\"{obj_input_data['search_data']}\" "
            
            cursor.execute(sql_search)

            list_request = cursor.fetchall() if cursor.rowcount > 0 else []

        response['code'] = 0
        response['list_request'] = list_request

    except Exception as e:
        print('search.models -> technicals_search -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response