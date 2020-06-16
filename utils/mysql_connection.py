import pymysql.cursors
from main import settings
from utils import global_config


def get_connection_info():
    connection = None
    try:
        connection = pymysql.connect(
            host=settings.MSQL_MOBILE_DEMO_INFO_HOST,
            port=int(settings.MSQL_MOBILE_DEMO_INFO_POST),
            db=settings.MSQL_MOBILE_DEMO_INFO_DB,
            user=settings.MSQL_MOBILE_DEMO_INFO_USER,
            password=settings.MSQL_MOBILE_DEMO_INFO_PASS,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

    except Exception as e:
        print('utils.mysql_connection -> get_connection_login_info -> ex: ', e)

    return connection
