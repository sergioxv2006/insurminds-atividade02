from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
import os

# 1. Carrega os embeddings (mesmo modelo usado antes)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Conecta ao banco ChromaDB existente (ajuste o caminho se necessário)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chroma_path = os.path.join(BASE_DIR, "chroma_db")

vectorstore = Chroma(persist_directory=chroma_path, embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 3. Inicializa o LLM (usando o phi3 para melhor otimização)
llm = OllamaLLM(model="phi3")

# 4. Prompt
template = """Use as seguintes partes de contexto recuperado do manual de seguros para responder à pergunta.
Se você não souber a resposta, diga que não encontrou a informação nas apólices.
Mantenha a resposta educada e concisa.

Contexto: {context}

Pergunta: {question}

Resposta do Atendente:"""
prompt = PromptTemplate.from_template(template)

def gerar_resposta_seguro(pergunta):
    docs_relevantes = retriever.invoke(pergunta)
    contexto_formatado = "\n\n".join(doc.page_content for doc in docs_relevantes)
    
    prompt_formatado = prompt.invoke({"context": contexto_formatado, "question": pergunta})
    resposta = llm.invoke(prompt_formatado)
    
    return resposta