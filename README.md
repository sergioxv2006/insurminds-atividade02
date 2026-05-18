markdown_content = """# 🚗 BPMSP Seguros S.A - Chatbot de Atendimento

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.2-092E20)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)
![Gemini](https://img.shields.io/badge/LLM-Google_Gemini-4285F4)

Projeto desenvolvido para o curso **InsurMinds - Agentes Inteligentes com Redes Generativas**, focado na criação de um assistente virtual inteligente para o mercado de seguros automotivos.

---

## 🎯 Objetivo Geral
Desenvolver um ChatBot de Atendimento automatizado utilizando a arquitetura **RAG (Retrieval-Augmented Generation)**. O objetivo é permitir que a inteligência artificial consulte manuais, apólices e regras de negócio internas da seguradora para responder de forma precisa, contextualizada e humanizada a dúvidas sobre coberturas, assistência 24h, sinistros e franquias, reduzindo a carga da equipe humana de atendimento.

## 👥 Usuários-Alvo
* **Segurados BPMSP:** Clientes buscando respostas rápidas sobre suas apólices, como regras de carro reserva ou cobertura para danos naturais.
* **Corretores de Seguros:** Profissionais que precisam consultar rapidamente regras de aceitação e limites de cobertura.
* **Equipe de Triagem:** Atendentes que recebem os casos mais complexos após a triagem e resolução de dúvidas primárias feitas pelo bot.

## ✨ Características do Projeto
* **Integração LLM em Nuvem:** Utiliza o modelo Gemini 1.5 Flash via API para alta velocidade e baixo consumo de hardware local.
* **Busca Vetorial (RAG):** Respostas baseadas estritamente nos documentos oficiais da seguradora, mitigando o risco de "alucinações" da IA.
* **Interface Web (Estilo WhatsApp):** Front-end responsivo com dark mode e botões interativos para uma experiência de usuário familiar.
* **Conformidade com LGPD:** Fluxo inicial de atendimento que exige o consentimento do usuário antes da coleta e processamento de dados.
* **Roteamento Inteligente:** Capacidade de separar interações determinísticas (como botões e validação de CPF) de perguntas abertas geradas por IA.

---

## 📁 Estrutura de Arquivos

O projeto está organizado na seguinte estrutura de diretórios:

```text
📦 BPMSP-Chatbot
 ┣ 📂 .git/                  # Diretório do repositório Git
 ┣ 📂 chat/                  # App principal do Django (Views, URLs, Templates)
 ┃ ┣ 📜 rag_service.py       # Motor RAG conectando LangChain, ChromaDB e Gemini
 ┃ ┗ 📂 templates/           # Arquivos de interface HTML/JS
 ┣ 📂 chroma_db/             # Banco de dados vetorial local (Armazena os embeddings)
 ┣ 📂 core/                  # Configurações globais do projeto Django (settings, urls)
 ┣ 📂 venv/                  # Ambiente virtual Python isolado
 ┣ 📜 .env                   # Variáveis de ambiente (Chave da API do Google)
 ┣ 📜 .gitignore             # Arquivos ignorados pelo controle de versão
 ┣ 📜 AVISO DE SINISTRO.docx # Base de conhecimento: Regras de sinistro
 ┣ 📜 BASE DE SEGURADOS.docx # Base de conhecimento: Dados de clientes
 ┣ 📜 Modelo Chatbot...docx  # Base de conhecimento: Fluxos do bot
 ┣ 📜 base de dados...docx   # Base de conhecimento: Regras gerais
 ┣ 📜 db.sqlite3             # Banco de dados relacional (Django)
 ┣ 📜 listar_modelos.py      # Script utilitário para checar modelos da API
 ┣ 📜 manage.py              # Orquestrador de comandos do Django
 ┗ 📜 requirements.txt       # Lista de dependências e bibliotecas do projeto
