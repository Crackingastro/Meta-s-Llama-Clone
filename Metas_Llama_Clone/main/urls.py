from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("home", views.home, name = 'home'),
    path("chat_gpt", views.chat_gpt, name = "chat_gpt"),
    path("image_to_text", views.image_to_text, name = "image_to_text"),
]