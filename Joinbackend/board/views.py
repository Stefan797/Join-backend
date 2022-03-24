from django.contrib.auth.models import User
from django.shortcuts import render

# from django.http import JsonResponse

# from django.core import serializers

# Create your views here.

def index(request):
    return render(request, 'board/index.html')
    
