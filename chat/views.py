from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .rag_service import gerar_resposta_seguro
from django.shortcuts import render
from django.views.generic import TemplateView

# View para carregar a interface visual
class ChatIndexView(TemplateView):
    template_name = 'chat/index.html'

class ChatBotAPIView(APIView):
    def post(self, request):
        pergunta = request.data.get("pergunta")
        
        if not pergunta:
            return Response({"erro": "A pergunta é obrigatória."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Chama o serviço RAG que está carregado na memória
            resposta_ia = gerar_resposta_seguro(pergunta)
            return Response({"resposta": resposta_ia}, status=status.HTTP_200_OK)
        except Exception as e:
            # IMPRIME O ERRO NO TERMINAL PARA PODEMOS DEPURAR
            print(f"\n--- ERRO NA IA --- \n{str(e)}\n-------------------\n")
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)