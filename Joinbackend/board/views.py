from django.contrib.auth.models import User
from django.shortcuts import render

from django.http import JsonResponse

from django.core import serializers

from board.models import Tasks

# Create your views here.

def index(request):
    return render(request, 'board/index.html')

def jsonboard(request):
    if request.method == 'POST':
        board_message = Tasks.objects.get(id=2)
        serialized_obj = serializers.serialize('json', [ board_message, ])
        return JsonResponse(serialized_obj[1:-1], safe=False)

def jsonabc(request):
    if request.method == 'GET':
        board_message = Tasks.objects.get(id=2)
        serialized_obj = serializers.serialize('json', [ board_message, ])
        return JsonResponse(serialized_obj[1:-1], safe=False)


# /api/tasks
# [{...}]
    
