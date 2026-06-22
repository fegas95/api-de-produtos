# 🛒 Products API

API REST para cadastro e gerenciamento de produtos, desenvolvida com FastAPI e Python.

## 🚀 Funcionalidades

- `POST /products` — Cadastrar novo produto
- `GET /products` — Listar todos os produtos
- `GET /products/{id}` — Buscar produto por ID
- `PATCH /products/{id}` — Atualizar produto parcialmente
- `DELETE /products/{id}` — Remover produto

## 🛠️ Tecnologias

- Python 3.10+
- FastAPI
- Pydantic (validação de dados)
- Uvicorn (servidor ASGI)

## ▶️ Como executar

```bash
# Clone o repositório
git clone https://github.com/fegas95/api-de-produtos.git
cd products-api

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
uvicorn main:app --reload
```

Acesse **http://localhost:8000/docs** para ver a documentação interativa gerada automaticamente pelo FastAPI.

## 📸 Documentação automática

O FastAPI gera uma interface Swagger UI em `/docs` onde você pode testar todos os endpoints diretamente pelo navegador, sem precisar de ferramentas externas.

## 📁 Estrutura do projeto

```
products-api/
├── main.py           # Endpoints da API
├── models.py         # Schemas de validação (Pydantic)
├── requirements.txt  # Dependências do projeto
└── README.md
```
