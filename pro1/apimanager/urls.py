from django.urls import path

from . import views

urlpatterns = [
    path('', views.apivoverview, name='apivoverview'),
    path('createUser', views.create_userApi, name='apiCreateUser'),
    path('apilistUsers', views.listUsers, name='apiListUsers'),
    path('deleteUser/<int:pk>', views.deleteUser, name='apiDeleteUser'),
    path('UpdateUser/<int:pk>', views.updateUser, name='apiUpdateUser'),
    # path('searchByName', views.ViewAllUser.as_view(), name='listUsers'),
]
