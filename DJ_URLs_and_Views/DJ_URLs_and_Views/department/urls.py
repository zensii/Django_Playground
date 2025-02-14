from django.urls import path, re_path

from DJ_URLs_and_Views.department import views

urlpatterns = [
    path('', views.index),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),
    path('<int:id>/<slug:slug>/', views.view_with_id_and_slug),  # can have multiple variables
    path('home/<variable>/', views.view_with_name),
    path('<param>/', views.view_with_args_and_kwargs),
    path('index/<int:pk>/', views.view_with_pk),
    path('<path:variable>', views.view_with_name), # type path will take the full path including /
    # path('<uuid:id>', some_view),

]