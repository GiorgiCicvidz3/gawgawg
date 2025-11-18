from django.urls import path
from . import views

urlpatterns = [
    path('computers/', views.computer_list, name='computer_list'),
]