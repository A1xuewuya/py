# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from models import *


# Create your views here.

def index(request):
    # view = loader.get_template("booktest/index.html")
    # return HttpResponse(view.render())

    # context = {"title": "index模板"}
    # return render(request, "booktest/index.html", context)

    content = dict(
        booklist=BookInfo.objects.all()
    )
    return render(request, "booktest/index.html", content)


def show(request, id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    content = dict(
        herolist=herolist
    )
    return render(request, "booktest/show.html", content)
