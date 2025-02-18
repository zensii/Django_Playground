from django.shortcuts import render

# Create your views here.

def register(request):

    return render(request, template_name='accounts/register-page.html')

def login(request):

    return render(request, template_name='accounts/login-page.html')


def show_profile(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
