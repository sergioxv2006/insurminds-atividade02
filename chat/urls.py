from django.urls import path
from .views import ChatBotAPIView, ChatIndexView

urlpatterns = [
    path('', ChatIndexView.as_view(), name='chat_home'), # Página inicial do chat
    path('api/perguntar/', ChatBotAPIView.as_view(), name='chatbot_api'), # Endpoint da API
]