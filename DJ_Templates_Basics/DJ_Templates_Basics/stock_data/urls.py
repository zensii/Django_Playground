from django.urls import path
from DJ_Templates_Basics.stock_data.views import stock_chart

urlpatterns = [
       path('', stock_chart, name='stock_home_page'),

]