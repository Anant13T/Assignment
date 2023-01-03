from .import views
from django.urls import path

urlpatterns = [
    path('<str:id>/',views.getData),
]
