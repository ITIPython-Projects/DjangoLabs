
from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('form', views.formPage, name='displayForm'),
   path('update/<int:proid>', views.updateProduct, name='updateProduct'),
   path('delete/<int:proid>', views.deleteProduct, name='deleteProduct'),
]