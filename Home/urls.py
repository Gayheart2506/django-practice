from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='index'),
    path("dave", views.dave_blog, name='dave-blog'),
    path("gayheart", views.gayheart_blog, name='gayheart-blog'),
]