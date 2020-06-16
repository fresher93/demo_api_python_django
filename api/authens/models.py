from utils import mysql_connection, response_json



def requester_login(username, password):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)

    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_select_requester = "SELECT * FROM requesters WHERE user_name=%s"
        cursor.execute(sql_select_requester, username)

        if cursor.rowcount == 0:
            response['code'] = 1

        elif cursor.rowcount == 1:
            data_user = cursor.fetchone()

            if password != data_user['password']:
                response['code'] = 2
            else:
                response['code'] = 0

    except Exception as e:
        print('authen.models -> requester_login -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response


def technical_login(username, password):
    connection = None
    cursor = None
    response = response_json.get_response_common(None, None)
    try:
        connection = mysql_connection.get_connection_info()
        cursor = connection.cursor()

        sql_select_technical = "SELECT * FROM technicals WHERE user_name=%s"
        cursor.execute(sql_select_technical, username)

        if cursor.rowcount == 0:
            response['code'] = 1

        elif cursor.rowcount == 1:
            data_user = cursor.fetchone()

            if password != data_user['password']:
                response['code'] = 2
            else:
                response['code'] = 0

    except Exception as e:
        print('authen.models -> technical_login -> ex: ', e)

    finally:
        if connection is not None:
            connection.close()

        if cursor is not None:
            cursor.close()

    return response
