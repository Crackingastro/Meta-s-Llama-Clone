from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_gpt, name = 'chat_gpt'),
    path("home", views.chat_gpt, name = 'chat_gpt'),
    path("chat_gpt", views.chat_gpt, name = "chat_gpt"),
]