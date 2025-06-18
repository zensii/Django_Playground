from django.shortcuts import render, redirect

from Exam_Prep_2.cars.forms import CarForm
from Exam_Prep_2.cars.models import Car
from Exam_Prep_2.utils import get_usr_obj


# Create your views here.

def catalogue(request):
    user = get_usr_obj()
    cars = user.cars.all()

    context = {
        'cars': cars,
    }

    return render(request, 'cars/catalogue.html', context)


def create_car(request):

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = get_usr_obj()
            car.save()
            return redirect('catalogue')
    else:
        form = CarForm()

    context = {
        'form': form,
        }

    return render(request, 'cars/car-create.html', context)



def edit_car(request, id):

    car = Car.objects.get(id=id)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarForm(instance=car)
    context = {
        'form': form,
    }

    return render(request, 'cars/car-edit.html', context)


def delete_car(request, id):

    car = Car.objects.get(id=id)
    form = CarForm(instance=car)

    for name, field in form.fields.items():
        if name == "type":
            field.widget.attrs["disabled"] = True
        else:
            field.widget.attrs["readonly"] = True

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'cars/car-delete.html', context)


def car_details(request, id):
    car = Car.objects.get(id=id)
    context = {
        'car': car,
    }
    return render(request, 'cars/car-details.html', context)