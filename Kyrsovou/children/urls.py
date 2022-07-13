from django.urls import path
from . import views

urlpatterns = [
    path('', views.child, name='child'),
    path('<int:pk>', views.detail.as_view(), name='dinam_chil'),
]