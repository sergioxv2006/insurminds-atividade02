from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

import os
from dotenv import load_dotenv

# 0. Carrega a chave de API do arquivo .env com segurança
load_dotenv()

# 1. Carrega os embeddings (mantemos o local para os vetores)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Conecta ao banco ChromaDB existente
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chroma_path = os.path.join(BASE_DIR, "chroma_db")

vectorstore = Chroma(persist_directory=chroma_path, embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 3. Inicializa o LLM na nuvem (Gemini)
# Ele vai puxar automaticamente a GOOGLE_API_KEY do seu ambiente
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 4. Prompt
template = """Use as seguintes partes de contexto recuperado do manual de seguros para responder à pergunta.
Se você não souber a resposta, diga que não encontrou a informação nas apólices.
Mantenha a resposta educada e concisa.

Contexto: {context}

Pergunta: {question}

Resposta do Atendente:"""
prompt = PromptTemplate.from_template(template)

def gerar_resposta_seguro(pergunta):
    # Busca no banco vetorial
    docs_relevantes = retriever.invoke(pergunta)
    contexto_formatado = "\n\n".join(doc.page_content for doc in docs_relevantes)
    
    # Formata a pergunta com o contexto
    prompt_formatado = prompt.invoke({"context": contexto_formatado, "question": pergunta})
    
    # Envia para o Gemini
    resposta = llm.invoke(prompt_formatado)
    
    # Diferente do Ollama, o Gemini retorna um objeto complexo.
    # Precisamos extrair apenas o texto final usando .content
    return resposta.content