from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('message/sent', views.sent, name="sent"),
]