from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.renderers import JSONRenderer
from main import jwt_custom_authen
from . import models, contants


# Begin Requester region


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def requester_login(request, format=None):
    response = contants.get_response_login(None)
    try:
        data_input = request.data

        username = data_input['username']
        password = data_input['password']

        data_output = models.requester_login(username, password)

        code_ouput = data_output['code']

        response = contants.get_response_login(code_ouput)

    except Exception as e:
        print('authen.views -> requester_login -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def requester_logout(request, format=None):
    response = contants.get_response_logout(None)
    try:
        print(1)

    except Exception as e:
        print('authen.views -> requester_logout -> ex: ', e)

    return Response(response)


# Begin Technical region


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def technical_login(request, format=None):
    response = contants.get_response_login(None)
    try:
        data_input = request.data

        username = data_input['username']
        password = data_input['password']

        data_output = models.technical_login(username, password)

        code_ouput = data_output['code']
        response = contants.get_response_login(code_ouput)

    except Exception as e:
        print('authen.views -> technical_login -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def technical_logout(request, format=None):
    response = contants.get_response_logout(None)
    try:
        print(1)

    except Exception as e:
        print('authen.views -> technical_logout -> ex: ', e)

    return Response(response)
