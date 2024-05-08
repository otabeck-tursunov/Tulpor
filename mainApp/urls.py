from django.urls import path
from .views import *

urlpatterns = [
    path('taomlar/', TaomlarView.as_view(), name='taomlar'),
    path('taomlar/<int:pk>/o\'chirish/', ToamOchirish.as_view()),
    path('ichimliklar/', IchimliklarView.as_view(), name='ichimliklar'),
    path('ichimliklar/<int:pk>/o\'chirish/', IchimlikOchirish.as_view()),
    path('joylar/', JoylarView.as_view(), name='joylar'),
    path('joylar/<int:pk>/o\'chirish/', JoyOchirish.as_view()),
]
