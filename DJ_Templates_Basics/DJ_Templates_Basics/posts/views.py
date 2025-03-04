from django.shortcuts import render, redirect

# Create your views here.
from datetime import datetime

from django.http import HttpResponse

from DJ_Templates_Basics.posts.forms import PersonForm, SearchForm
from DJ_Templates_Basics.posts.model_forms import PostForm, PostDeleteForm
from DJ_Templates_Basics.posts.models import Post


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


def model_add_post(request):

    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        'form': form,
    }

    return render(request, 'posts/model_add_post.html', context)


def dashboard(request):

    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = posts.filter(title__icontains=query)
    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, 'posts/dashboard.html', context)


def select_post_to_delete(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        selected_post_id = request.POST.get('post_id')
        return redirect('delete_post', pk = selected_post_id)

    return render(request, 'posts/select_delete.html', {'posts':  posts})
def delete_post(request, pk: int):
    post = Post.objects.get(pk = pk)

    if request.method == 'POST':
        post.delete()
        return redirect('dash')

    deleted_form = PostDeleteForm(instance=post)  # here we fill in the form with data from the DB. In this case the form we want to delete.

    context = {
        'form': deleted_form,
        'post': post,
    }

    return render(request, 'posts/delete_post.html', context)


def details_page(request, pk:int):
    post = Post.objects.all()
    context = {
        'posts': post,
    }
    return render(request, 'posts/details-post.html', context)

