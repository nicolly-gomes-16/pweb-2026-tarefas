from django.urls import path
from . import views

urlpatterns = [
    path("", views.deveres, name="deveres"),
]
