from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Message
from .forms import MessageForm

class Home(TemplateView):
    template_name = "chat_rooms/home.html"


class ChatRoomView(ListView):
    model = Message
    template_name = "chat_rooms/chat_room.html"
    context_object_name = "messages_context"


class PostMessageView(CreateView):

    model = Message
    form_class = MessageForm

    template_name = "chat_rooms/new_message.html"
    success_url = reverse_lazy("chat_rooms:chatroom_list")


