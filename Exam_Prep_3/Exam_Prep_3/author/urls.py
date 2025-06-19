from django.urls import path

from Exam_Prep_3.author.views import author_create, author_details, author_edit, author_delete

urlpatterns = [
    path('create/', author_create, name='author-create'),
    path('details/', author_details, name='author-details'),
    path('edit/', author_edit, name='author-edit'),
    path('delete/', author_delete, name='author-delete'),
]