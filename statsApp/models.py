from django.core.validators import MinLengthValidator
from django.db import models
from mainApp.models import *


class Buyurtma(models.Model):
    raqam = models.AutoField(primary_key=True)
    joy = models.ForeignKey(Joy, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    hisoblandi = models.PositiveIntegerField(default=0)
    tolandi = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    def __str__(self):
        return f"{self.joy}. Buyurtma raqami: {self.raqam}"


class BuyurtmaIchimlik(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)
    ichimlik = models.ForeignKey(Ichimlik, on_delete=models.CASCADE)
    soni = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Ichimlik'
        verbose_name_plural = 'Ichimliklar'

    def jami(self):
        return self.ichimlik.narx * self.soni


class BuyurtmaTaom(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)
    taom = models.ForeignKey(Taom, on_delete=models.CASCADE)
    soni = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Taom'
        verbose_name_plural = 'Taomlar'


    def jami(self):
        return self.taom.narx * self.soni
