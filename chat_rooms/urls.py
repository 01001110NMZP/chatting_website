from django.urls import path
from .views import Home, ChatDisplayCreateView

app_name = "chat_rooms"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("chatroom/", ChatDisplayCreateView.as_view(), name="selected_chatroom"),
]