from django.urls import path

from DJ_Templates_Basics.current_time.views import index, welcome_page

urlpatterns = [
       path('', welcome_page, name='home_page'),
       path('time/', index, name='time_page'),
]
