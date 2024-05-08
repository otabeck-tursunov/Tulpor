from django.urls import path
from .views import *

urlpatterns = [
    path('buyurtmalar/', BuyurtmalarView.as_view(), name='buyurtmalar'),
    path('buyurtmalar/<int:pk>/', BuyurtmaView.as_view()),
    path('buyurtmalar/<int:pk>/o\'chirish/', BuyurtmaOchirish.as_view()),
]