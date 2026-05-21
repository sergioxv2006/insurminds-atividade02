# 0. O que esse script faz?
# Ele lista os modelos de IA disponíveis para a sua conta do Google.
# Serve para consultar os modelos disponíveis para o Chatbot.

import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Carrega a sua chave do arquivo .env
load_dotenv()
chave_api = os.getenv("GOOGLE_API_KEY")

# 2. Configura a conexão
genai.configure(api_key=chave_api)

print("Consultando a API do Google...\n")
print("Modelos liberados para a sua conta gerar textos:")
print("-" * 50)

# 3. Pede a lista oficial e filtra os que servem para o Chatbot
try:
    for modelo in genai.list_models():
        if 'generateContent' in modelo.supported_generation_methods:
            print(f"Nome do modelo: {modelo.name}")
except Exception as e:
    print(f"Erro ao consultar: {e}")