from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.http import HttpResponse



def index(request):

    context = {
        "current_time": datetime.now(),
        "person": {
            "age": 20,
            "height": 190,
        },
        "ids": ["62348764", "fwhj827634", "42y3tyr"],
        "some_text": "Hello",
        "users": [
            "pesho",
            "ivan",
            "stamat",
            "saria",
            "magdalena"
        ]
    }

    return render(request, 'posts/base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project?",
                "author": "Some Author",
                "content": "I **really** don't how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 1?",
                "author": "",
                "content": "### <i>I really don't know how</i> to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 2?",
                "author": "Some Author",
                "content": "",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)