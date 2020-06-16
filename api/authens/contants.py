from rest_framework import status


def get_response_login(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later!',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Logged in successfully'
        elif code == "1":
            response['message'] = 'Account does not exist'
        elif code == "2":
            response['message'] = 'Wrong password'

    return response


def get_response_logout(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later!',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Logged out successfully'
        elif code == 777:
            response['message'] = 'Token does not exist'

    return response
