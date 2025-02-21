from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def welcome_page(request):

    return render(request, 'current_time/welcome.html')


def index(request):

    return render(request, 'current_time/time.html')

def test(request):

    return render(request, 'current_time/test.html')