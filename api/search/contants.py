from rest_framework import status


def getResponseProfile(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'user_info': {}
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'OK'

    return response
