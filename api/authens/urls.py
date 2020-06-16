from django.urls import path
from . import views

urlpatterns = [
    path('authen/requester/login', views.requester_login),
    path('authen/requester/logout', views.requester_logout),
    # Technical url
    path('authen/technical/login', views.technical_login),
    path('authen/technical/logout', views.technical_logout)
]
