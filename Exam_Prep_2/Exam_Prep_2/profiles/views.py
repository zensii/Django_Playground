from django.shortcuts import render, redirect

from Exam_Prep_2.cars.models import Car
from Exam_Prep_2.profiles.forms import ProfileBaseForm, ProfileEditForm
from Exam_Prep_2.utils import get_usr_obj
# Create your views here.


def index(request):

    return render(request, 'index.html')

def create_profile(request):

    if request.method == 'POST':
        form = ProfileBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileBaseForm()

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-create.html', context)



def edit_profile(request):

    user = get_usr_obj()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileEditForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):

    user = get_usr_obj()

    if request.method == 'POST':
        user.delete()
        return redirect('index')

    return render(request, 'profiles/profile-delete.html')


def profile_details(request):

    user = get_usr_obj()
    cars = user.cars.all()
    total_price = sum(car.price for car in cars)

    if user.first_name and user.last_name:
        full_name = user.first_name + ' ' + user.last_name
    elif user.first_name:
        full_name = user.first_name
    else:
        full_name = user.last_name

    context = {
        'user': user,
        'total_price': total_price,
        'full_name': full_name,
    }

    return render(request, 'profiles/profile-details.html', context)