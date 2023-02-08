from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
from django.http import HttpResponse

def index(r):
    context = {}
    context['products'] = Product.objects.all()
    if context['products'] != '':
        return render(r, "app1pages/index.html",context)
    else:
        return render(r, "app1pages/index.html",{'empty':1})

def formPage(r):
    return render(r, "app1pages/form.html")

def updateProduct(r,proid):
    context = {}
    if(r.method == 'GET'):
        pro = Product.objects.get(id=proid)
        context['product'] = pro
        return render(r, "app1pages/updateproduct.html", context)
    else:
        new = r.POST
        pro = Product.objects.filter(id=proid).update(name=new['name'])
        return HttpResponseRedirect("/")

def deleteProduct(r,proid):
    Product.objects.filter(id=proid).delete()
    return HttpResponseRedirect("/")