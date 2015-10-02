from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    context = {}
    return render(request, 'home.html', context)
