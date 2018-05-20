from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader


# Create your views here.

def index(request):
    view = loader.get_template("booktest/index.html")
    return HttpResponse(view.render())
