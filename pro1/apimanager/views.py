from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def apivoverview(r):
    api_urls = {
        'get_allUser': '/all/',
        'Create User': 'create/'
    }
    return Response({'code': status.HTTP_200_OK}, data=api_urls)


@api_view(['POST'])
def create_userApi(r):
    pass


@api_view(['GET'])
def listUsers(r):
    pass


@api_view(['DELETE'])
def deleteUser(r, pk):
    pass


@api_view(['PUT'])
def updateUser(r, pk):
    pass
