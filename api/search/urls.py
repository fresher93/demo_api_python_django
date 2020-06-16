from django.urls import path
from . import views

urlpatterns = [
    path('requesters/search/', views.requesters_search),
    path('technicals/search/', views.technicals_search),
]
