from django.urls import path

from Petstagram.accounts.views import register, login, show_profile, edit_profile, delete_profile

urlpatterns = [    #  must be named URL patterns
    # we just add the url path and the name of the view for this page,
    path('register/', register, name='register_account' ),
    path('login/', login, name='user_login' ),
    path('profile/<int:pk>/', show_profile, name='show_user_profile' ),
    path('profile/<int:pk>/edit/', edit_profile, name='edit_user_profile' ),
    path('profile/<int:pk>/delete/', delete_profile, name='delete_user_profile' ),
]