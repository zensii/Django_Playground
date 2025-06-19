from django.shortcuts import render, redirect

from Exam_Prep_3.author.forms import AuthorCreationForm, AuthorEditForm
from Exam_Prep_3.author.models import Author


# Create your views here.

def author_create(request):
    if request.method == 'POST':
        form = AuthorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
    else:
        form = AuthorCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'author/create-author.html', context)

def author_details(request):

    author = Author.objects.first()
    context = {
        'author': author,
        'profile_pic': author.image_url,
        'full_name': f"{author.first_name} {author.last_name}",
        'posts_count': author.posts.count(),
        'pets_count': author.pets_number,
        'last_post': author.posts.last() if author.posts.exists() else 'N/A'
    }

    return render(request, 'author/details-author.html', context)

def author_edit(request):

    author = Author.objects.first()
    if request.method == 'POST':
        form = AuthorEditForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-details')
    else:
        form = AuthorEditForm(instance=author)

    context = {
    'form': form,
    'author': author,
    }
    return render(request, 'author/edit-author.html', context)

def author_delete(request):
    author = Author.objects.first()
    if request.method == 'POST':
        author.delete()
        return redirect('index-page')

    return render(request, 'author/delete-author.html')
