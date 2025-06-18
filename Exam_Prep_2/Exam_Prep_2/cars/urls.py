from django.urls import path

from Exam_Prep_2.cars.views import catalogue, create_car, car_details, edit_car, delete_car

urlpatterns = [
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create_car, name='create_car'),
    path('<int:id>/details/', car_details, name='car_details'),
    path('<int:id>/edit/', edit_car, name='edit_car'),
    path('<int:id>/delete/', delete_car, name='delete_car'),
]