from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_app(request):
    return HttpResponse('this is first app')

