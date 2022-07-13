from django.urls import path
from . import views

urlpatterns = [
    path('', views.nachalo,name='home'),


]
