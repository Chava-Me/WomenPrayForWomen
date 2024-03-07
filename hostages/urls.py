from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_page),
    path('new', views.new_page)
]