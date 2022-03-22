from django.shortcuts import render

# from django.http import JsonResponse

# from django.core import serializers

# Create your views here.

def index(request):
    # if request.method == 'POST':
    #     serialized_obj = serializers.serialize('json', [ obj, ])
    return render(request, 'board/index.html')
    
