from django.contrib import admin
from django.urls import path, include
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('main/', include('mainApp.urls')),
    path('stats/', include('statsApp.urls')),
]
