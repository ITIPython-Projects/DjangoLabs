from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import RegisterForm
from .models import UserData
from django.contrib.auth.models import  User
from django.contrib.auth import  authenticate,login,logout
from django.views.decorators.http import require_GET
from  django.views import View
from django.views.generic import ListView
from rest_framework import serializers
# Create your views here.
class LoginViewClass(View):
    def post(self,r):
        value = UserData.objects.filter(username=r.POST['name'], password=r.POST['password'])
        adminUser = authenticate(username=r.POST['name'], password=r.POST['password'])
        if len(value) > 0:
            r.session['userid'] = value[0].id
            r.session['username'] = r.POST['name']
            if adminUser is not None:
                login(r, adminUser)
            return render(r, 'pages/userpage.html')
        else:
            return render(r, 'pages/Login.html', {'error': 1})
    def get(self,r):
        return HttpResponse("Get Not Allowd")
def registerPage(r):
    return render(r, 'pages/register.html',{'regsForm':RegisterForm})

def loginPage(r):
    return render(r, 'pages/Login.html')

def registerOperation(r):
    if (r.method == 'POST'):
        RegisterForm(r.POST).save()
        #User.objects.create_user(r.POST)
        #User.objects.create_user(username=r.POST['username'],email=r.POST['email'],
        #                        password=r.POST['password'])
        return HttpResponseRedirect('/')

def loginOperation(r):
    if(r.method=='POST'):
        value = UserData.objects.filter(username=r.POST['name'], password=r.POST['password'])
        adminUser = authenticate(username=r.POST['name'], password=r.POST['password'])
        if len(value) > 0:
            r.session['userid'] = value[0].id
            r.session['username'] = r.POST['name']
            if adminUser is not None:
                login(r,adminUser)
            return render(r, 'pages/userpage.html')
        else:
            return render(r, 'pages/Login.html',{'error':1})
    else:
        return HttpResponse("Hi")

@require_GET
def mylogOut(r):
    #Logut Operations
    r.session.clear()
    return HttpResponseRedirect('/')

#viewAllUser
class ViewAllUser(ListView):
    model = UserData
