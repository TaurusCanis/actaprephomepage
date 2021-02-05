from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_message/', views.submit_message, name='submit_message'),
]
