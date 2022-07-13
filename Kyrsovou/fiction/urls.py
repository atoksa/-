from django.urls import path
from . import views

urlpatterns = [
    path('', views.fiction, name='fiction'),
    path('<int:pk>', views.detail.as_view(), name='dinam_fic'),
]