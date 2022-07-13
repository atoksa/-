from django.urls import path
from . import views

urlpatterns = [
    path('', views.detective, name='detective'),
    path('<int:pk>', views.detail.as_view(), name='dinam_detec'),
]