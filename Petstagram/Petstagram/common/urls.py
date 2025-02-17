from django.urls import path

from Petstagram.common.views import home_page

urlpatterns = [    #  must be named URL patterns
    # we just add the url path and the name of the view for this page,
    path('', home_page, name='home_page'),
]