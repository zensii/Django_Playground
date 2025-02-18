
from django.urls import path
from DJ_Templates_Basics.posts.views import dashboard, index

urlpatterns = [
    path('posts/', index, name='index'),
    path('posts/dashboard/', dashboard, name='dash'),
]
