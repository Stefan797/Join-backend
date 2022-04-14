from django.dispatch import receiver
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from board.models import Tasks
import json 

# Create your views here.

# Wenn der User bereits angemeldet ist 
# @login_required(login_url='/login/')
# def index(request):
#     if request.method == 'POST':
        
# Login Funktion 
# def login_view(request): 
#     redirect = request.GET.get('next')
#     if request.method == 'POST':
#         user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
#         if user:
#             login(request, user)
#             print('request.GET.get(next)', request.GET.get('next'))
#             return HttpResponseRedirect(request.POST.get('redirect'))
#         else:
#             return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
#     return render(request, 'auth/login.html', {'redirect': redirect})

# Registrirung eines neuen Accounts 
# def register_view(request):
#     if request.method == 'POST': 
#         if request.POST.get('password') == request.POST.get('repeated_password'):
#             user = User.objects.create_user(username=request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
#         else:
#             return render(request, 'auth/register.html', {'wrongPassword': True}) # Todo: Fehlermeldung zurückgeben
#     return render(request, 'auth/register.html', )

def index(request):
    if request.method == 'POST':
        new_task = Tasks.objects.create(text=request.POST['textvalue'], user=request.user, created_at=request.POST['datevalue'], color=request.POST['colorvalue'], discription=request.POST['discriptionvalue'], category=request.POST['category'])
    
    return render(request, 'board/index.html')



def jsononeelement(request, id):
    if request.method == 'GET':
        board_message = Tasks.objects.get(id=id)
        # board_message = Tasks.objects.all()
        #board_msg_json = json.loads(board_message) 
        serialized_obj = serializers.serialize('json', [ board_message, ])
        return HttpResponse(serialized_obj[1:-1], content_type='application/json')
        # return JsonResponse(serialized_obj[1:-1], safe=False)
    

def jsonlist(request):
    if request.method == 'GET':
        fulljson = Tasks.objects.all()
        # print('das hier ist', fulljson)
        serialized_obj = serializers.serialize('json', fulljson,)
        # print(serialized_obj)
        return HttpResponse(serialized_obj[1:-1], content_type='application/json')
        #return JsonResponse(serialized_obj[1:-1], safe=False)

