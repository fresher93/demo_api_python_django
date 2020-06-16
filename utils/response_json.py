from rest_framework import status


def get_response_common(code, message):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK
    }

    if code is not None:
        response['code'] = code

    if message is not None:
        response['message'] = message

    return response
