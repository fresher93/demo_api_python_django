from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.decorators import parser_classes
from rest_framework.renderers import JSONRenderer
from . import models, contants


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def regist_requesters(request, format=None):
    response = contants.get_response_regist(None)
    try:
        request_data = request.data

        obj_data_input = {
            "user_name": request_data['username'],
            "password": request_data['password']
        }

        data_output = models.regist_requesters(obj_data_input)
        code_output = data_output['code']

        response = contants.get_response_get_data_search(code_output)

    except Exception as e:
        print('regist.views -> regist_requesters -> ex: ', e)

    return Response(response)
