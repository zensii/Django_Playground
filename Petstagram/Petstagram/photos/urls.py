from django.urls import path

from Petstagram.photos.views import add_photo, show_photo, edit_photo

urlpatterns = [    #  must be named URL patterns
    # we just add the url path and the name of the view for this page,
    path('add/', add_photo, name='add_pet_photo'),
    path('<int:pk>', show_photo, name='show_pet_photo'),
    path('<int:pk>/edit/', edit_photo, name='edit_pet_photo'),

]