from django.http import  HttpResponse
from django.shortcuts import render
from .models import Hostage

import os
import sys

def index(request):
    hostages = list(Hostage.objects.all())
    hostages = hostages+hostages
    hostages = hostages + hostages
    hostages = hostages + hostages
    isHebrew = True
    if request.path == '/home/en':
        isHebrew=False
        for val in hostages:
            if val.english_name != '':
                val.name = val.english_name
            if val.english_info != '':
                val.info = val.english_info
    return render(request,
                   'index.html',
                   {'hostages': hostages, 'isHebrew': isHebrew})


def new_page(request):
    return HttpResponse('New Product')

