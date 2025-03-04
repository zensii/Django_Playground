
from django.urls import path, include
from DJ_Templates_Basics.posts.views import dashboard, index, model_add_post, delete_post, select_post_to_delete, \
    details_page

urlpatterns = [
    path('posts/', index, name='index'),

    path('model-posts-add', model_add_post, name='model-add-post'),
    path('posts/dashboard/', dashboard, name='dash'),
    path('delete-post/', select_post_to_delete, name='select_post_to_delete'),
    path('<int:pk>/', include([
        path('delete-post/', delete_post, name='delete_post'),
        path('details-post/', details_page, name='details-post')
        ])
    )




]
