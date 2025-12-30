from django.urls import path
from .views import Home, ChatRoomView, PostMessageView

app_name = "chat_rooms"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("chatroom/", ChatRoomView.as_view(), name="chatroom_list"),
    path("chatroom/new_message", PostMessageView.as_view(), name="chatroom_post")
]