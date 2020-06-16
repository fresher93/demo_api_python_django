from django.urls import path
from . import views

urlpatterns = [
    # get_data_search
    path('claim/get_data_claim_group', views.btn_get_data_claim_group),
    # get_data_search
    path('claim/get_data_operator', views.btn_get_data_operator),
    # btnClaim_Search_Click
    path('claim/btn_search_click', views.btn_claim_search_click),
    # get_data_selected
    path('claim/get_data_selected', views.btn_claim_get_data_selected),
    # btnClaimAddBtnReg
    path('claim/btn_add_click', views.btn_claim_add_click),
    # btnClaimEditClickBtnReg
    path('claim/btn_edit_click', views.btn_claim_edit_click),
    # btnClaimDelClick
    path('claim/btn_del_click', views.btn_claim_del_click),

    # get_data_selected
    path('claim/group/get_data_selected', views.btn_claim_group_get_data_selected),
    # btnAddClaimGroup
    path('claim/group/btn_add_click', views.btn_claim_group_add_click),
    # btnEditClaimGroup
    path('claim/group/btn_edit_click', views.btn_claim_group_edit_click),
    # btnDelClaimGroup
    path('claim/group/btn_del_click', views.btn_claim_group_del_click),
    # btnDelClaimGroup
    path('claim/group/get_caim_count', views.get_claim_count),
    path('claim/group/sort', views.click_sort_down_row),
    path('claim/group/get_claim_group', views.get_selected_claim),
    path('claim/import_csv', views.btn_import_csv_click),
]
