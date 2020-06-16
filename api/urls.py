from django.urls import path, include

urlpatterns = [
    path('api/', include('api.claims.urls')),
    path('api/', include('api.authens.urls')),
    path('api/', include('api.search.urls'))
]
