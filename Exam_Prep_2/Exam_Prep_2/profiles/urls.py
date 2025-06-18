from django.urls import path

from Exam_Prep_2.profiles.views import create_profile, profile_details, edit_profile, delete_profile

urlpatterns = [
    path('create/', create_profile, name='profile_create'),
    path('details/', profile_details, name='profile_details'),
    path('edit/', edit_profile, name='profile_edit'),
    path('delete/', delete_profile, name='profile_delete'),
]