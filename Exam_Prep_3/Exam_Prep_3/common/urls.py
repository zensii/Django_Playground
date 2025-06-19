from django.urls import path

from Exam_Prep_3.common.views import index, dashboard

urlpatterns = [
    path('', index, name='index-page'),
    path('dashboard/', dashboard, name='dashboard-page'),
]