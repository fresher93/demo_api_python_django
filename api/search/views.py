from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.decorators import parser_classes
from rest_framework.renderers import JSONRenderer
from . import models
from . import contants


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def requesters_search(request, format=None):
    response = contants.getResponseProfile(None)
    try:

        data_request = request.data

        obj_input_data = {
            "user_id": data_request["user_id"],
            "search_type": data_request["search_type"],
            "search_data": data_request["search_data"]
        }

        data_output = models.requesters_search(obj_input_data)

        code_ouput = data_output['code']
        list_request = data_output['list_request']

        response = contants.getResponseProfile(code_ouput)
        response['list_request'] = list_request

    except Exception as e:
        print('search.views -> requesters_search -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def technicals_search(request, format=None):
    response = contants.getResponseProfile(None)
    try:

        data_request = request.data

        obj_input_data = {
            "user_id": data_request["user_id"],
            "search_type": data_request["search_type"],
            "search_data": data_request["search_data"]
        }

        data_output = models.technicals_search(obj_input_data)

        code_ouput = data_output['code']
        list_request = data_output['list_request']

        response = contants.getResponseProfile(code_ouput)
        response['list_request'] = list_request

    except Exception as e:
        print('search.views -> technicals_search -> ex: ', e)

    return Response(response)