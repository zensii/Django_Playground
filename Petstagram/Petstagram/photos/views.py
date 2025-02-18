from django.shortcuts import render

# Create your views here.
def add_photo(request):
    return render(request, template_name='photos/photo-add-page.html')

def show_photo(request, pk):
    return render(request, template_name='photos/photo-details-page.html')

def edit_photo(request, pk):
    return render(request, template_name='photos/photo-edit-page.html')

def view_photo(request, pk):
    return render(request, '<img>{% Photo.id %}</img>')