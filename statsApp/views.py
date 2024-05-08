from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import *


class BuyurtmalarView(View):
    def get(self, request):
        buyurtmalar = Buyurtma.objects.order_by('tolandi').order_by('-raqam')
        context = {'buyurtmalar': buyurtmalar}
        return render(request, 'buyurtmalar.html', context)


class BuyurtmaOchirish(View):
    def get(self, request, pk):
        Buyurtma.objects.get(raqam=pk).delete()
        return redirect('buyurtmalar')


class BuyurtmaView(View):
    def get(self, request, pk):
        buyurtma = Buyurtma.objects.get(raqam=pk)
        return render(request, 'buyurtma.html', {'buyurtma': buyurtma})
