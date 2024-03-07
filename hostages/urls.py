from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('en', views.index),
    path('he', views.index),
    path('new', views.new_page)
]