from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from main import jwt_custom_authen, settings
from utils import global_config


class PermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            url_request = request.META['PATH_INFO']
            ip_request = request.META['REMOTE_ADDR']
            server_name = request.META['SERVER_NAME']

            print(url_request)
            print(ip_request)
            print(server_name)

            global_config.GLB_USER_IP_ADDRESS = ip_request
            global_config.GLB_USER_PC_NAME = server_name

            url_access_request = settings.EVERCALL_API_URL_ACCESS
            url_access_request_flag = False
            for val1 in url_access_request:
                if url_request == val1:
                    url_access_request_flag = True
                    break

            if not url_access_request_flag:
                token_request = request.META['HTTP_AUTHORIZATION']
                flag_check_token = jwt_custom_authen.verify_token(token_request)

                if flag_check_token:
                    permission_access_request = settings.EVERCALL_API_PERMISSION_ACCESS
                    permission_access_request_flag = False
                    for val2 in permission_access_request:
                        if url_request.find(val2) != -1:
                            permission_access_request_flag = True
                            break

                    if not permission_access_request_flag:
                        flag_check_permission = jwt_custom_authen.permission_token(token_request, url_request)

                        if not flag_check_permission:
                            return JsonResponse(
                                {
                                    "code": 555,
                                    "message": "You do not have access to this api"
                                }
                            )
                else:
                    return JsonResponse(
                        {
                            "code": 333,
                            "message": "Token is incorrect"
                        }
                    )
        except Exception as e:
            print('Filter middleware: error -> ', e)
            return JsonResponse(
                {
                    "code": 333,
                    "message": "Token is incorrect"
                }
            )

    def process_response(self, request, response):
        if response.status_code != 200:
            return JsonResponse(
                {
                    "code": response.status_code,
                    "message": "ERROR"
                }
            )

        return response
