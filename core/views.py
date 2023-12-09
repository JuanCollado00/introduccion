from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(sellf, request, *arge, **kwargs):
        context={

        }
        return render(request, 'index.html',context)