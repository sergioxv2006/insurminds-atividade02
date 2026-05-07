# pyrefly: ignore [missing-import]
from langchain_ollama import OllamaLLM

# Conecta ao modelo Llama 3 usando a nova classe
llm = OllamaLLM(model="llama3")

print("Enviando pergunta para a IA...")
resposta = llm.invoke("Responda em uma frase: O que é um seguro de automóvel?")

print("\nResposta do Llama 3:")
print(resposta)