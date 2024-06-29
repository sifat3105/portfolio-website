from django.urls import path
from .views import home_view, about_create, success_page

urlpatterns = [
    path('',home_view, name="home"),
    path('about/', about_create, name='about_create'),
    path('success/', success_page, name='success_page'),
]
