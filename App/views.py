from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
from App.forms import *

# Create your views here.

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic data inserted successfully')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WPO=WebpageForm()
    d1={'WPO':WPO}

    if request.method=='POST':
        WPDO=WebpageForm(request.POST)
        if WPDO.is_valid():
            WPDO.save()
            return HttpResponse('Webpage data inserted successfully')
    return render(request,'insert_webpage.html',d1)

def insert_ar(request):
    ARO=AccessRecordForm()
    d2={'ARO':ARO}

    if request.method=='POST':
        ARDO=AccessRecordForm(request.POST)
        if ARDO.is_valid():
            ARDO.save()
            return HttpResponse('AccessRecord data inserted successfully')
    return render(request,'insert_ar.html',d2)