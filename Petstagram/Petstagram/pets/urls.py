from django.urls import path

from Petstagram.pets.views import add_pet, view_pets, edit_pet, delete_pet

urlpatterns = [    #  must be named URL patterns
    # we just add the url path and the name of the view for this page,
    path('add/', add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/', view_pets, name='view_pet_details'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', edit_pet, name='edit_pet'),
    path('<str:username>/pet/<slug:pet_slug>/delete/', delete_pet, name='delete_pet'),

]