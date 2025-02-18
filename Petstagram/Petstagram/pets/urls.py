from django.urls import path, include

from Petstagram.pets.views import add_pet, view_pets, edit_pet, delete_pet

urlpatterns = [    #  must be named URL patterns
    # we just add the url path and the name of the view for this page,
    path('add/', add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/',include([
        path('', view_pets, name='view_pet_details'),
        path('edit/', edit_pet, name='edit_pet'),
        path('delete/', delete_pet, name='delete_pet')
        ])
    )
]