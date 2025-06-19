from django.urls import path

from Exam_Prep_3.posts.views import post_create, post_details, post_edit, post_delete

urlpatterns = [
    path('create/', post_create, name='post-create'),
    path('<int:pk>/details/', post_details, name='post-details'),
    path('<int:pk>/edit/', post_edit, name='post-edit'),
    path('<int:pk>/delete/', post_delete, name='post-delete'),
]