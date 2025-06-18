from django.urls import path

from Exam_prep1.albums.views import add_album, album_details, edit_album, delete_album

app_name = 'albums'

urlpatterns = [
    path('album/add/', add_album, name='add_album'),
    path('album/<int:pk>/details/', album_details, name='album_details'),
    path('album/<int:pk>/edit/', edit_album, name='edit_album'),
    path('album/<int:pk>/delete/', delete_album, name='delete_album'),
]