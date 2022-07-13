from django.urls import path
from . import views

urlpatterns = [
    path('', views.zar_lit, name='zar_lit'),
    path('<int:pk>', views.detail.as_view(), name='dinam'),



]
