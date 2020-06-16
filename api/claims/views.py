# File: claims.views.py
# Description: map call api to claims FE
# Author                                Date                                         Change Description
# NLQHuy, HMThu                         2020/04/08                                   Create new
# NLQHuy                                2020/05/09                                   Fix bug claim search, load combobox operator

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.renderers import JSONRenderer
from . import models, contants


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_get_data_claim_group(request, format=None):
    response = contants.get_response_get_data_search(None)
    try:
        data_output = models.btn_get_data_claim_group()

        code_output = data_output['code']
        data_claimgroup = data_output['data_claimgroup']

        response = contants.get_response_get_data_search(code_output)
        response['data_claimgroup'] = data_claimgroup

    except Exception as e:
        print('claims.views -> btn_get_data_claim_group -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_get_data_operator(request, format=None):
    response = contants.get_response_get_data_search(None)
    try:
        data_output = models.btn_get_data_operator()

        code_output = data_output['code']
        data_claim_user = data_output['data_claim_user']

        response = contants.get_response_get_data_search(code_output)
        response['data_claim_user'] = data_claim_user
    except Exception as e:
        print('claims.views -> btn_get_data_claim_group -> ex: ', e)

    return Response(response)


@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_claim_search_click(request, format=None):
    response = contants.get_response_data_search(None)
    try:
        data_input = request.data
        obj_data_input = {
            "claim_create_date_check": request.data["claim_create_date_check"],
            "claim_create_date_start": request.data["claim_create_date_start"],
            "claim_create_date_end": request.data["claim_create_date_end"],
            "claim_group_id": data_input['claim_group_id'],
            "user_id": data_input['user_id'],
            "name": data_input['name'],
            "tel_for_find": data_input['tel_for_find'],
            "biko": data_input['biko'],
            'limit_cnt': data_input['limit_cnt'],
            'row_current_page': data_input['row_current_page'],
            'row_per_page': data_input['row_per_page'],
            'btn_flag_click': data_input['btn_flag_click'],
            'cg_name_kensaku': data_input['cg_name_kensaku'],
            'name_kensaku': data_input['name_kensaku'],
            'tel_kensaku': data_input['tel_kensaku'],
        }
        data_output = models.btn_claim_search_click(obj_data_input)
        code_output = data_output['code']
        data_search_table = data_output['data_search_table']
        response = contants.get_response_data_search(code_output)
        response['data_search_table'] = data_search_table
        response['table_total_row'] = data_output['table_total_row']
    except Exception as e:
        print('claims.views -> btn_claim_search_click -> ex: ', e)

    return Response(response)


# ---btn_claim_get_data_selected
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_claim_get_data_selected(request, format=None):
    response = contants.get_response_get_data_search(None)
    try:
        data_input = request.data
        id = data_input['id']

        data_output = models.btn_claim_get_data_selected(id)

        code_output = data_output['code']
        data_claim_obj = data_output['data_claim_obj']

        response = contants.get_response_get_data_search(code_output)
        response['data_claim_obj'] = data_claim_obj

    except Exception as e:
        print('claims.views -> btn_claim_get_data_selected -> ex: ', e)

    return Response(response)


# ---btn_claim_add_click
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_claim_add_click(request, format=None):
    response = contants.get_response_claim_add(None)
    try:
        data_input = request.data
        if data_input['claim_group_id'] == 0 or data_input['claim_group_id'] == "" or data_input['claim_group_id'] is None:
            response = contants.get_response_claim_add("ER09.3-02")
        else:
            if len(data_input['name']) > 255:
                response = contants.get_response_claim_add("MS09.303")
            elif len(data_input['tel']) > 20:
                response = contants.get_response_claim_add("MS09.304")
            elif len(data_input['biko']) > 1000:
                response = contants.get_response_claim_add("MS09.305")
            else:
                obj_data_input = {
                    "claim_group_id": data_input['claim_group_id'],
                    "name": data_input['name'],
                    "tel": data_input['tel'],
                    "biko": data_input['biko']
                }

                data_output = models.btn_claim_add_click(obj_data_input)
                code_output = data_output['code']
                response = contants.get_response_claim_add(code_output)
    except Exception as e:
        print('claims.views -> btn_claim_add_click -> ex: ', e)

    return Response(response)


# ---btn_claim_edit_click
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_claim_edit_click(request, format=None):
    response = contants.get_response_claim_edit(None)
    try:
        data_input = request.data
        if data_input['claim_group_id'] == 0 or data_input['claim_group_id'] == "" or data_input['claim_group_id'] is None:
            response = contants.get_response_claim_edit("ER09.3-02")
        else:
            if len(data_input['name']) > 255:
                response = contants.get_response_claim_edit("MS09.303")
            elif len(data_input['tel']) > 20:
                response = contants.get_response_claim_edit("MS09.304")
            elif data_input['biko'] is not None and data_input['biko'] != '':
                if len(data_input['biko']) > 1000:
                    response = contants.get_response_claim_edit("MS09.305")
                else:
                    obj_data_input = {
                        "name": data_input['name'],
                        "tel": data_input['tel'],
                        "claim_group_id": data_input['claim_group_id'],
                        "biko": data_input['biko'],
                        "id": data_input['id']
                    }
                    data_output = models.btn_claim_edit_click(obj_data_input)
                    code_output = data_output['code']
                    response = contants.get_response_claim_edit(code_output)
    except Exception as e:
        print('claims.views -> btn_claim_edit_click -> ex: ', e)

    return Response(response)


# ---btn_claim_del_click
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_claim_del_click(request, format=None):
    response = contants.get_response_claim_del(None)
    try:
        data_input = request.data

        data_output = models.btn_claim_del_click(data_input['claim_group_id'])

        code_output = data_output['code']

        response = contants.get_response_claim_del(code_output)

    except Exception as e:
        print('claims.views -> btn_claim_del_click -> ex: ', e)

    return Response(response)


# ---btn_claim_group_get_data_selected
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_claim_group_get_data_selected(request, format=None):
    response = contants.get_response_get_data_selected(None)
    try:
        data_output = models.btn_claim_group_get_data_selected()

        code_output = data_output['code']
        data_claim_group = data_output['data_claim_group']

        response = contants.get_response_get_data_selected(code_output)
        response['data_claim_group'] = data_claim_group
    except Exception as e:
        print('claims.views -> btn_claim_group_get_data_selected -> ex: ', e)

    return Response(response)


# ---btn_claim_group_add_click
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_claim_group_add_click(request, format=None):
    response = contants.get_response_claim_group_add(None)
    try:
        data_input = request.data
        if len(data_input['name']) > 255:
            response = contants.get_response_claim_group_add("MS09.201")
        else:
            obj_data_input = {
                "name": data_input['name']
            }
            data_output = models.btn_claim_group_add_click(obj_data_input)
            code_output = data_output['code']
            response = contants.get_response_claim_group_add(code_output)
    except Exception as e:
        print('claims.views -> btn_claim_group_add_click -> ex: ', e)

    return Response(response)


# ---btn_claim_group_edit_click
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_claim_group_edit_click(request, format=None):
    response = contants.get_response_claim_group_edit(None)
    try:
        data_input = request.data
        if len(data_input['name']) > 255:
            response = contants.get_response_claim_group_add("MS09.201")
        else:
            obj_data_input = {
                "name": data_input['name'],
                "claim_group_id": data_input['claim_group_id']
            }
            data_output = models.btn_claim_group_edit_click(obj_data_input)
            code_output = data_output['code']
            response = contants.get_response_claim_group_edit(code_output)
    except Exception as e:
        print('claims.views -> btn_claim_group_edit_click -> ex: ', e)

    return Response(response)


# ---btn_claim_group_del_click
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_claim_group_del_click(request, format=None):
    response = contants.get_response_claim_group_del(None)
    try:
        data_input = request.data
        claim_group_id = data_input['claim_group_id']

        data_output = models.btn_claim_group_del_click(claim_group_id)

        code_output = data_output['code']
        response = contants.get_response_claim_group_del(code_output)
    except Exception as e:
        print('claims.views -> btn_claim_group_del_click -> ex: ', e)

    return Response(response)


# ---getClaimCount
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def get_claim_count(request, format=None):
    response = contants.get_response_data_search(None)
    try:
        # data_input = request.data

        data_output = models.get_claim_count()

        code_output = data_output['code']
        data_get_claim_count = data_output['data_get_claim_count']

        response = contants.get_response_data_search(code_output)
        response['data_get_claim_count'] = data_get_claim_count
    except Exception as e:
        print('claims.views -> btn_claim_group_del_click -> ex: ', e)

    return Response(response)


# function: click_sort_down_row
# parameter: request - json type
# return: json status code
# description: load form setting
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def click_sort_down_row(request):
    response = contants.get_response_sort(None)
    try:
        data_input = request.data
        obj_data_input = {
            'flag': data_input['flag'],
            'claim_group_id': data_input['claim_group_id'],
            'sort': data_input['sort'],
        }
        record_output = models.set_sort_up_down(obj_data_input)
        code_response = record_output['code']
        response['code'] = code_response
    except Exception as ex:
        response['exception'] = ex.args
        print('prospects.views -> click_sort_down_row -> ex: ', ex)

    return Response(response)


# function: get_selected_claim
# parameter: request - json type
# return: json status code
# description: get selected claim row
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def get_selected_claim(request):
    response = contants.get_response_sort(None)
    try:
        data_input = request.data
        record_output = models.get_selected_claim(data_input['claim_group_id'])
        response['selected_claim'] = record_output['selected_claim']
        response['code'] = record_output['code']
    except Exception as ex:
        response['exception'] = ex.args
        print('prospects.views -> get_selected_claim -> ex: ', ex)

    return Response(response)


# function: btn_import_csv_click
# parameter: request - json type
# return: json status code
# description: import csv
@api_view(['POST'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def btn_import_csv_click(request):
    response = contants.get_response_import_csv(None)
    try:
        data_input = request.data
        record_output = models.import_csv_claim(data_input['claim_group_id'], data_input['claim_list'])

        response['code'] = record_output['code']
        response['cnt'] = record_output['cnt']
    except Exception as ex:
        response['exception'] = ex.args
        print('prospects.views -> btn_import_csv_click -> ex: ', ex)

    return Response(response)
