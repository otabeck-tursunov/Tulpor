from django.shortcuts import render, redirect
from django.views import View

from .models import *


class BolimlarView(View):
    def get(self, request):
        return render(request, 'bolimlar.html')


class TaomlarView(View):
    def get(self, request):
        taomlar = Taom.objects.order_by('nom')
        context = {
            'taomlar': taomlar
        }
        return render(request, 'taomlar.html', context)

    def post(self, request):
        Taom.objects.create(nom=request.POST['nom'], narx=request.POST['narx'])
        return redirect('taomlar')


class ToamOchirish(View):
    def get(self, request, pk):
        Taom.objects.get(pk=pk).delete()
        return redirect('taomlar')


class IchimliklarView(View):
    def get(self, request):
        ichimliklar = Ichimlik.objects.order_by('nom')
        context = {
            'ichimliklar': ichimliklar
        }
        return render(request, 'ichimliklar.html', context)

    def post(self, request):
        Ichimlik.objects.create(nom=request.POST['nom'], narx=request.POST['narx'])
        return redirect('ichimliklar')


class IchimlikOchirish(View):
    def get(self, request, pk):
        Ichimlik.objects.get(pk=pk).delete()
        return redirect('ichimliklar')


class JoylarView(View):
    def get(self, request):
        joylar = Joy.objects.order_by('raqam')
        context = {
            'joylar': joylar
        }
        return render(request, 'joylar.html', context)

    def post(self, request):
        Joy.objects.create(raqam=request.POST['raqam'], orin=request.POST['orin'])
        return redirect('joylar')


class JoyOchirish(View):
    def get(self, request, pk):
        Joy.objects.get(pk=pk).delete()
        return redirect('joylar')
