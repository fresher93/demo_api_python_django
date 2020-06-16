from rest_framework import status


def get_response_get_data_search(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Display data successful'
        elif code == "ER0901":
            response['message'] = 'Enter the time is incorrect.'
        elif code == "ER0902":
            response['message'] = 'No data can be retrieved.'
        elif code == "MS0901":
            response['message'] = 'The search may take some time because the condition is not set. Continue processing as it is now?.'
        elif code == "MS0902":
            response['message'] = 'Data export completed.'
        elif code == "MS0903":
            response['message'] = 'Please select the data to delete.'
        elif code == "MS0904":
            response['message'] = 'Removed complaint information.If you want to reflect as a complaint, please register again. Completed delete.'

    return response


def get_response_get_data_operator_group(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Display data successful'
        elif code == "ER0902":
            response['message'] = 'No data can be retrieved.'
    return response


def get_response_data_search(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            "claim_create_date_check": "1/0",
            "claim_create_date_start": "Date",
            "claim_create_date_end": "Date",
            "claim_group_id": "String",
            "user_id": "String",
            "name": "String",
            "tel": "String",
            "biko": "String"
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Display data successful'
        elif code == "ER0901":
            response['message'] = 'Enter the time is incorrect.'
        elif code == "ER0902":
            response['message'] = 'No data can be retrieved.'
        elif code == "MS0901":
            response['message'] = 'The search may take some time because the condition is not set. Continue processing as it is now?.'
        elif code == "MS0902":
            response['message'] = 'Data export completed.'
        elif code == "MS0903":
            response['message'] = 'Please select the data to delete.'
        elif code == "MS0904":
            response['message'] = 'Removed complaint information.If you want to reflect as a complaint, please register again. Completed delete.'
    return response


def get_response_get_data_selected(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            "claim_group_id": "int"
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Display data successful'
        elif code == "ER0902":
            response['message'] = 'No data can be retrieved.'
    return response


def get_response_claim_add(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            "claim_group_id": "int not null",
            "name": "String",
            "tel": "String",
            "tel_for_find": "String",
            "user_id": "int",
            "biko": "String",
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Added successfully'
        elif code == "ER09.301":
            response['message'] = 'Please enter the phone number.'
        elif code == "ER09.302":
            response['message'] = 'Please select a request group'
        elif code == "MS09.301":
            response['message'] = 'Request information & results. Done'
        elif code == "MS09.302":
            response['message'] = 'Because no conditions are set, it may take time to search. Do you want to continue processing?'
        elif code == "MS09.303":
            response['message'] = 'Length of name cannot over 255 digits'
        elif code == "MS09.304":
            response['message'] = 'Length of tel cannot over 20 digits'
        elif code == "MS09.305":
            response['message'] = 'Length of biko cannot over 1000 digits'
        elif code == "ER09.3-02":
            response['message'] = 'Please select claim group'
        elif code == "ER09.3-03":
            response['message'] = 'Duplicate entry'
        elif code == "ER09.3-04":
            response['message'] = 'Phone number was existed'

    return response


def get_response_claim_edit(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            "id": "int not null",
            "name": "int not null",
            "tel": "int not null",
            "tel_for_find": "String",
            "user_id": "int",
            "biko": "int",
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Edit successfully'
        elif code == "ER09.301":
            response['message'] = 'Please enter the phone number.'
        elif code == "ER09.302":
            response['message'] = 'Please select a request group'
        elif code == "MS09.301":
            response['message'] = 'Request information & results. Done'
        elif code == "MS09.302":
            response['message'] = 'Because no conditions are set, it may take time to search. Do you want to continue processing?'
        elif code == "MS09.303":
            response['message'] = 'Length of name cannot over 255 digits'
        elif code == "MS09.304":
            response['message'] = 'Length of tel cannot over 20 digits'
        elif code == "MS09.305":
            response['message'] = 'Length of biko cannot over 1000 digits'
        elif code == "ER09.3-02":
            response['message'] = 'Please select claim group'
        elif code == "ER09.3-03":
            response['message'] = 'Duplicate entry'
        elif code == "ER09.3-04":
            response['message'] = 'Phone number was existed'
    return response


def get_response_claim_del(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            'id': 'int'
        }
    }
    if code is not None:
        response['code'] = code
        if code == "CF0901":
            response['message'] = 'Delete complaint information. After deletion, can not be restored?'
        elif code == 0:
            response['message'] = 'Claim deleted'
    return response


def get_response_claim_group_add(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            'name': 'String'
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Added successfully'
        elif code == "ER09.101":
            response['message'] = 'Please enter group name'
        elif code == "ER09.102":
            response['message'] = 'Group home name has been registered'
        elif code == "CF09.101":
            response['message'] = 'Asking for a registered group name, Do you want to continue?'
        elif code == "CF09.102":
            response['message'] = 'Delete request group name, are you sure?'
        elif code == "MS09.101":
            response['message'] = 'Changed to request group name. Finished'
        elif code == "MS09.102":
            response['message'] = 'The group name request has been deleted.'
        elif code == "MS09.201":
            response['message'] = 'Length of group name cannot over 255 digits'
    return response


def get_response_claim_group_edit(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            'name': 'String'
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Edited successfully'
        elif code == "ER09.101":
            response['message'] = 'Please enter group name'
        elif code == "ER09.102":
            response['message'] = 'Group home name has been registered'
        elif code == "CF09.101":
            response['message'] = 'Asking for a registered group name, Do you want to continue?'
        elif code == "CF09.102":
            response['message'] = 'Delete request group name, are you sure?'
        elif code == "MS09.101":
            response['message'] = 'Changed to request group name. Finished'
        elif code == "MS09.102":
            response['message'] = 'The group name request has been deleted.'
        elif code == "MS09.201":
            response['message'] = 'Length of group name cannot over 255 digits'
    return response


def get_response_claim_group_del(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            'claim_group_id': 'int'
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Claim group deleted'
        elif code == "ER09.101":
            response['message'] = 'Please enter group name'
        elif code == "ER09.102":
            response['message'] = 'Group home name has been registered'
        elif code == "CF09.101":
            response['message'] = 'Asking for a registered group name, Do you want to continue?'
        elif code == "CF09.102":
            response['message'] = 'Delete request group name, are you sure?'
        elif code == "MS09.101":
            response['message'] = 'Changed to request group name. Finished'
        elif code == "MS09.102":
            response['message'] = 'The group name request has been deleted.'
    return response


def get_response_get_phone_line(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            'user_group_id': 'int',
            'extensions_group_id': 'int'
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Display data successful'
    return response


def get_response_phone_line(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            'user_group_id': 'int',
            'extensions_group_id': 'int'
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Setting changed'
    return response


# function: get_response_sort
# parameter: code - int
# return: code value and notification message
# description: show message with corresponding code to user
def get_response_sort(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'json_data_input': {
            'flag': 'int',
            'claim_group_id': 'int'
        }
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Sort successfully'
    return response


# function: get_response_sort
# parameter: code - int
# return: code value and notification message
# description: show message with corresponding code to user
def get_response_selected_row(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'claim_group_id': 'int'
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Sort successfully'
    return response


# function: get_response_import_csv
# parameter: code - int
# return: code value and notification message
# description: show message with corresponding code to user
def get_response_import_csv(code):
    response = {
        'code': 999,
        'message': 'System busy, please try again later !',
        'status_code': status.HTTP_200_OK,
        'claim_group_id': 'int'
    }
    if code is not None:
        response['code'] = code
        if code == 0:
            response['message'] = 'Import csv successfully'
    return response
