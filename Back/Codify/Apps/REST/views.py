from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from Apps.REST.serializers import UserSerializer
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import os
from django.contrib.auth import authenticate, login
# Create your views here.



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({"Error":"Favor de completar los campos"}, status = HTTP_404_NOT_FOUND)
    user = User.objects.filter(username=username, password=password).first()
    if not user:
        return Response({"Error":"Credenciales no válidas"}, status = HTTP_400_BAD_REQUEST)
    else:
        token, _ = Token.objects.get_or_create(user=user)
        request.session['sesion'] = user.id
        # authenticate(username=username, password=password)
        # print(authenticate)
        # login(request, user)
        request.user = username
        return Response({"token":token.key, "user":user.id}, status=HTTP_200_OK)

def logout(request):
    try:
        del request.session['sesion']
    except KeyError:
        pass
    return redirect("/")

@permission_classes((AllowAny,))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail = False)
    def recent_users(self, request):
        recent_users = User.all().order_by('date_joined')
        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)