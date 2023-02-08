from django.urls import path
from . import views
urlpatterns = [
   path('register', views.registerPage, name='registerPage'),
   path('registerSave', views.registerOperation, name='registerSave'),
   path('login', views.loginPage, name='loginPage'),
   path('loginOperation', views.LoginViewClass.as_view(), name='loginOperation'),
   path('userLogout', views.mylogOut, name='userLogout'),
   path('listUsers', views.ViewAllUser.as_view(), name='listUsers'),
]