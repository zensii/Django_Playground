from django.urls import path

from Exam_prep1.profiles.views import profile_details, profile_delete

app_name = 'profiles'

urlpatterns = [
    path('profile/details/', profile_details, name='profile_details'),
    path('profile/delete/', profile_delete, name='profile_delete'),
]