from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.http import HttpResponse

from DJ_Templates_Basics.posts.forms import PersonForm


def index(request):

    form = PersonForm(request.POST or None)  # here we say : we get a post request , we get alldata from the request and crete a form with the data. If no data exists we get an empty form
    if request.method == 'POST':
        print(request.POST['person_name'])

    if form.is_valid():  # validates the form and returns errors and clean_data
        print(form.cleaned_data['person_name'])


    context = {
        'my_form': form
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