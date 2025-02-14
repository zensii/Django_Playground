from django.http import HttpResponse
from django.shortcuts import render, redirect

from DJ_URLs_and_Views.department.models import Department


# Create your views here.

def index(request):
    return HttpResponse('Hello World')


def view_with_name(request, variable):
    return HttpResponse(f"<h1>Variable: {variable}</h1>")

def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args} Kwargs: {kwargs}</h1>")

def view_with_pk(request, pk: int):
    return HttpResponse(f"<h1>Int pk wth pk: {pk}</h1>")

def view_with_id_and_slug(request, id, slug):
    department = Department.objects.get(id=id, slug=slug)
    return HttpResponse(f"<h1>The department with id: {id} and slug: {slug} is {department}</h1>")

def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is {archive_year}</h1>")

def redirect_to_view(request):

    # redirect('http://localhost:8000/numbers/') this breaks the abstraction
    # redirect(index) breaks single responsibility if view is from another app
    # return redirect('home') # this is the best option. We need to give the view a name and refer to it
    return redirect('numbers', pk=2) # can be used with views that accept parameters as well