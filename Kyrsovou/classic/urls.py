from django.urls import path
from . import views

urlpatterns = [
    path('', views.classic, name='classic'),
    path('<int:pk>', views.detail.as_view(), name='dinam_clas'),
]