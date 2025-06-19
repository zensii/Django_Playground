from django.shortcuts import render, redirect

from Exam_Prep_3.author.models import Author
from Exam_Prep_3.posts.forms import PostCreateForm, PostDeleteForm
from Exam_Prep_3.posts.models import Post


# Create your views here.

def post_create(request):

    user = Author.objects.first()

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('dashboard-page')
    else:
        form = PostCreateForm()
    context = {
        'form': form,
    }

    return render(request, 'posts/create-post.html', context)

def post_details(request, pk):

    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'posts/details-post.html', context)

def post_edit(request, pk):

    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostCreateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
    else:
        form = PostCreateForm(instance=post)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'posts/edit-post.html', context)

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard-page')
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'posts/delete-post.html', context)