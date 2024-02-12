from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('my_results/', views.resultdiary, name="Gym results"),
]