from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "shop/shop.html")


def about(request):
    return HttpResponse(" in about ")


def contact(request):
    return HttpResponse(" in contact ")


def tracker(request):
    return HttpResponse(" in tracker ")


def search(request):
    return HttpResponse(" in search ")


def prodView(request):
    return HttpResponse(" in prodView ")


def checkout(request):
    return HttpResponse(" in checkout ")
