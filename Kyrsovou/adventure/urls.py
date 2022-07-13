from django.urls import path
from . import views

urlpatterns = [
    path('', views.adventure, name='adventure'),
    path('<int:pk>', views.detail.as_view(), name='dinam_adv'),
]