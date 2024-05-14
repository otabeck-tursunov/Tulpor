from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import *


class BuyurtmalarView(View):
    def get(self, request):
        buyurtmalar = Buyurtma.objects.order_by('tolandi').order_by('-raqam')
        joylar = Joy.objects.all()
        context = {
            'buyurtmalar': buyurtmalar,
            'joylar': joylar
        }
        return render(request, 'buyurtmalar.html', context)

    def post(self, request):
        Buyurtma.objects.create(
            joy=Joy.objects.get(id=request.POST['joy']),
        )
        return redirect('buyurtmalar')

class BuyurtmaOchirish(View):
    def get(self, request, pk):
        Buyurtma.objects.get(raqam=pk).delete()
        return redirect('buyurtmalar')


class BuyurtmaView(View):
    def get(self, request, pk):
        buyurtma = Buyurtma.objects.get(raqam=pk)
        btaomlar = BuyurtmaTaom.objects.filter(buyurtma=buyurtma)
        bichimliklar = BuyurtmaIchimlik.objects.filter(buyurtma=buyurtma)
        buyurtmalar = Buyurtma.objects.filter(tolandi=False)
        taomlar = Taom.objects.all()
        ichimliklar = Ichimlik.objects.all()
        context = {
            'buyurtma': buyurtma,
            'btaomlar': btaomlar,
            'bichimliklar': bichimliklar,
            'buyurtmalar': buyurtmalar,
            'taomlar': taomlar,
            'ichimliklar': ichimliklar
        }
        return render(request, 'buyurtma.html', context)

    def post(self, request, pk):
        buyurtma = Buyurtma.objects.get(raqam=pk)
        modal_post = request.POST.get('modal_post', None)
        if modal_post is not None:
            if modal_post == "taom":
                BuyurtmaTaom.objects.create(
                    buyurtma=buyurtma,
                    taom=Taom.objects.get(pk=request.POST.get('taom')),
                    soni=request.POST.get('miqdor')
                )
            elif modal_post == "ichimlik":
                BuyurtmaIchimlik.objects.create(
                    buyurtma=buyurtma,
                    ichimlik=Ichimlik.objects.get(pk=request.POST.get('ichimlik')),
                    soni=request.POST.get('miqdor')
                )

            def hisobla(a, b):
                return a * b

            t = sum(list(map(hisobla, buyurtma.buyurtmataom_set.values_list('taom__narx', flat=True), buyurtma.buyurtmataom_set.values_list('soni', flat=True))))
            i = sum(list(map(hisobla, buyurtma.buyurtmaichimlik_set.values_list('ichimlik__narx', flat=True), buyurtma.buyurtmaichimlik_set.values_list('soni', flat=True))))
            buyurtma.hisoblandi = t + i
            buyurtma.save()
        return redirect(f'/stats/buyurtmalar/{buyurtma.pk}/')


class BuyurtmaTaomDeleteView(View):
    def get(self, request, pk):
        btaom = BuyurtmaTaom.objects.filter(id=pk)
        buyurtma = btaom.first().buyurtma
        btaom.delete()
        return redirect(f'/stats/buyurtmalar/{buyurtma.pk}/')


class BuyurtmaIchimlikDeleteView(View):
    def get(self, request, pk):
        bichimlik = BuyurtmaIchimlik.objects.filter(pk=pk)
        buyurtma = bichimlik.first().buyurtma
        bichimlik.delete()
        return redirect(f'/stats/buyurtmalar/{buyurtma.pk}')
