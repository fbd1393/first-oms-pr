from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')


def products(request):
    return HttpResponse('Products')


def customers(request):
    return HttpResponse('Customers')
