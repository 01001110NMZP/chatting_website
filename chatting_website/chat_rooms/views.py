from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Message
from .forms import MessageForm

class Home(TemplateView):
    template_name = "chat_rooms/home.html"


class ChatDisplayCreateView(CreateView, ListView):
    model = Message
    form_class = MessageForm

    template_name = "chat_rooms/chat_room.html"
    context_object_name = "chat_data"

    success_url = reverse_lazy("chat_rooms:selected_chatroom")

    # gets all the objects made by the model
    def get_queryset(self):
        return Message.objects.all()

    """
    (I could say) injects the model objects into the get() implementation of the parent views
    
    the object_list must be pre-filled, meaning before the ListView even starts, because when 
    it does, it only searches for object_list, if there isnt such thing there will be a 
    AttributeError, try removing either get or post to see it
    """
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    # exact same stuff happened to get()
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)


    # this generates the context dictionary
    def get_context_data(self, **kwargs):

        # im not sure but does it save the dictionary into "context"?
        context = super().get_context_data(**kwargs)

        # checks if there are any forms in the context
        if "form" not in context:

            # CreateView  adds  form
            # ListView    adds  object_list
            context["form"] = self.get_form()

        return context

"""
    old views

class ChatRoomView(ListView):
    model = Message
    template_name = "chat_rooms/chat_room.html"
    context_object_name = "messages_context"


class PostMessageView(CreateView):

    model = Message
    form_class = MessageForm

    template_name = "chat_rooms/new_message.html"
    success_url = reverse_lazy("chat_rooms:chatroom_list")
"""

