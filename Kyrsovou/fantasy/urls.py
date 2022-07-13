from django.urls import path
from . import views

urlpatterns = [
    path('', views.fantasy, name='fantasy'),
    path('<int:pk>', views.detail.as_view(), name='dinam_fan'),
]