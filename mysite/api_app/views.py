from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# Create your views here.
@api_view(['POST'])
def log(request):
    username = request.data['username']
    password = request.data['password']
    user_val = login_user.objects.filter(log_user=username, password=password).exists()
    if user_val:
        return Response({"result":"successs"})
    else:
        return Response("Invalid username and password")
