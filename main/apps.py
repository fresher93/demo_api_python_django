from django.apps import AppConfig
# from utils import global_func_load
import sys


class AppGlobalConfig(AppConfig):
    name = 'main'

    # def ready(self):
        # try:
            # print('<<<<<-------------------------- StartUp --------------------------->>>>>')
            # print('========================================================================')

            # global_func_load.get_reload_db_login_info()  # 1
            # global_func_load.get_reload_db_evercall()  # 2

            # print('<<<<<--------------------------- Done ----------------------------->>>>>')
            # print('========================================================================')

        # except Exception as e:
        #    print('main.apps.AppGlobalConfig -> ready -> ex: ', e)
        #    sys.exit(0)
