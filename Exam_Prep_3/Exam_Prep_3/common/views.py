from django.shortcuts import render

from Exam_Prep_3.author.models import Author


# Create your views here.

def index(request):
    return render(request, 'common/index.html')

def dashboard(request):
    user = Author.objects.first()
    posts = user.posts.all()

    context = {
        'posts': posts,
    }
    return render(request, 'common/dashboard.html', context)