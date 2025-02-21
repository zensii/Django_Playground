from django.urls import path

from DJ_Templates_Basics.current_time.views import index, welcome_page, test

urlpatterns = [
       path('', welcome_page, name='home_page'),
       path('time/', index, name='time_page'),
       path('time/test/', test, name='test_page'),
]
