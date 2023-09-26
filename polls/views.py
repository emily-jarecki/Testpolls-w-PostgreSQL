from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import HttpResponse


def index(request):
    print(request)
    return render(request, "polls/index.html")