from main import settings
from datetime import datetime
import jwt
from utils import global_config

jwt_token_memory_authen = []


def create_token(userid, username, password, menu_access, ip_request, browser_request):
    time_now_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    payload = {
        'userid': userid,
        'username': username,
        'password': password,
        'time': time_now_str,
        'ip': ip_request,
        'browser': browser_request,
        'menu_access': menu_access
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode("utf-8")

    for obj_old in reversed(jwt_token_memory_authen):
        if obj_old['username'] == username:
            time_old_str = obj_old['time']

            time_old_fr = datetime.strptime(time_old_str, "%d-%m-%Y %H:%M:%S")
            time_now_fr = datetime.strptime(time_now_str, "%d-%m-%Y %H:%M:%S")

            duration_time = time_now_fr - time_old_fr
            duration_minutes = duration_time.seconds / 60

            if duration_minutes > 30:
                jwt_token_memory_authen.remove(obj_old)

    user_memory_jwt = {
        'userid': userid,
        'username': username,
        'password': password,
        'token': token,
        'time': time_now_str,
        'ip': ip_request,
        'browser': browser_request,
        'menu_access': menu_access
    }

    jwt_token_memory_authen.append(user_memory_jwt)

    return token


def verify_token(token):
    flag_check_done = False
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')

        userid = decoded['userid']
        username = decoded['username']
        password = decoded['password']
        ip_request = decoded['ip']
        browser_request = decoded['browser']

        for obj_old in jwt_token_memory_authen:
            if obj_old['username'] == username and obj_old['password'] == password and obj_old['ip'] == ip_request and obj_old['browser'] == browser_request and obj_old['token'] == token:
                time_old_str = obj_old['time']
                time_now_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                time_old_fr = datetime.strptime(time_old_str, "%d-%m-%Y %H:%M:%S")
                time_now_fr = datetime.strptime(time_now_str, "%d-%m-%Y %H:%M:%S")

                duration_time = time_now_fr - time_old_fr
                duration_minutes = duration_time.seconds / 60

                if duration_minutes > 30:
                    jwt_token_memory_authen.remove(obj_old)
                    flag_check_done = False
                else:
                    obj_old['time'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    global_config.GLB_USER_ID = userid
                    global_config.GLB_USER_NAME = username

                    flag_check_done = True

                break
    except Exception as e:
        print('Token incorrect', e)

    return flag_check_done


def get_all_session_user(token):
    arr_data_info = []
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        username = decoded['username']

        for obj_old in jwt_token_memory_authen:
            if obj_old['username'] == username and obj_old['token'] != token:
                obj_output = {
                    'username': obj_old['username'],
                    'ip': obj_old['ip'],
                    'time': obj_old['time'],
                    'browser': obj_old['browser']
                }
                arr_data_info.append(obj_output)

    except Exception as e:
        print('Token incorrect', e)

    return arr_data_info


def delete_token(token):
    flag_check_delete_done = False
    try:
        for obj_old in jwt_token_memory_authen:
            if obj_old['token'] == token:
                jwt_token_memory_authen.remove(obj_old)
                flag_check_delete_done = True
                break
    except Exception as e:
        print('Token incorrect', e)

    return flag_check_delete_done


def delete_user_token_time(token, time):
    flag_check_delete_done = False
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        username = decoded['username']

        for obj_old in jwt_token_memory_authen:
            if obj_old['username'] == username and obj_old['time'] == time:
                jwt_token_memory_authen.remove(obj_old)
                flag_check_delete_done = True
                break
    except Exception as e:
        print('Token incorrect', e)

    return flag_check_delete_done


def permission_token(token, url_request):
    flag = False
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        menu_access = decoded['menu_access']
        menu_setting_sub = menu_access['menu_setting_sub']

        if url_request.find('/rest/api/top') != -1:
            if menu_access['menu_top'] == 1:
                flag = True
        elif url_request.find('/rest/api/operator') != -1:
            if menu_access['menu_operator'] == 1:
                flag = True
        elif url_request.find('/rest/api/list') != -1:
            if menu_access['menu_list'] == 1:
                flag = True
        elif url_request.find('/rest/api/customer') != -1:
            if menu_access['menu_customer'] == 1:
                flag = True
        elif url_request.find('/rest/api/prospect') != -1:
            if menu_access['menu_prospect'] == 1:
                flag = True
        elif url_request.find('/rest/api/claim') != -1:
            if menu_access['menu_claim'] == 1:
                flag = True
        elif url_request.find('/rest/api/summary') != -1:
            if menu_access['menu_summary'] == 1:
                flag = True
        elif url_request.find('/rest/api/dataoutput') != -1:
            if menu_access['menu_dataoutput'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting') != -1:
            if menu_access['menu_setting'] == 1:
                flag = True
        elif url_request.find('/rest/api/evercatch') != -1:
            if menu_access['menu_evercatch'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/info') != -1:
            if menu_setting_sub['menu_setting_info'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/biko') != -1:
            if menu_setting_sub['menu_setting_biko'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/customerinfo') != -1:
            if menu_setting_sub['menu_setting_customerinfo'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/call') != -1:
            if menu_setting_sub['menu_setting_call'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/sharelabel') != -1:
            if menu_setting_sub['menu_setting_sharelabel'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/userviewset') != -1:
            if menu_setting_sub['menu_setting_userviewset'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/resultpattern') != -1:
            if menu_setting_sub['menu_setting_resultpattern'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/template') != -1:
            if menu_setting_sub['menu_setting_template'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/inform') != -1:
            if menu_setting_sub['menu_setting_inform'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/history') != -1:
            if menu_setting_sub['menu_setting_history'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/outputtemplate') != -1:
            if menu_setting_sub['menu_setting_outputtemplate'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/admin') != -1:
            if menu_setting_sub['menu_setting_admin'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/transfertel') != -1:
            if menu_setting_sub['menu_setting_transfertel'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/rebildtemplate') != -1:
            if menu_setting_sub['menu_setting_rebildtemplate'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/customerdetailtemplate') != -1:
            if menu_setting_sub['menu_setting_customerdetailtemplate'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/calltaskmanager') != -1:
            if menu_setting_sub['menu_setting_calltaskmanager'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/calltagmanager') != -1:
            if menu_setting_sub['menu_setting_calltagmanager'] == 1:
                flag = True
        elif url_request.find('/rest/api/setting/termsofservice') != -1:
            if menu_setting_sub['menu_setting_termsofservice'] == 1:
                flag = True

    except Exception as e:
        print('Token incorrect', e)

    return flag


def user_token(token):
    username = ''
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        username = decoded['username']
    except Exception as e:
        print('Token incorrect', e)

    return username
