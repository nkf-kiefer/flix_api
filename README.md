# 🍿 Projeto Flix API

API de catálogo de filmes construída com Python / Django REST Framework, publicada na PythonAnywhere e escrita seguindo as boas práticas da PEP 8.

Gerencie Atores, Filmes, Gêneros e Reviews com um CRUD completo, importação em massa via Excel e respostas JSON legíveis.

Esta é uma API desenvolvida como parte do curso de **Python/Django** realizado na **PycodeBR Treinamentos**. 

---

## 🚀 Funcionalidades

**Cadastro & Autenticação:** usuários organizados por grupos e permissões.

**CRUD completo:** crie, edite, busque e exclua Atores, Filmes, Gêneros e Reviews.

**Uploads de Imagem:** para atores e filmes

**Reviews de Filmes:** nome do filme, avaliação ⭐ e comentário.

**JSON "bonito":** os relacionamentos retornam nomes em vez de IDs crus.

**Comando Customizado:** import_actors para popular atores a partir de planilha .xlsx.

**Requisitos Separados:** requirements.txt e dev.txt

---

## 🛠️ Tecnologias Utilizadas

- Django 4 + Django REST Framework

- Python 3.11

- PostgreSQL (produção) | SQLite (desenvolvimento)

- PythonAnywhere para hospedagem

---

## 🌟 Pontos de Melhoria

- Testes automatizados (Pytest + DRF tests).

- Integração contínua com GitHub Actions.

- Paginação e filtros mais avançados na listagem de filmes.

- Endpoint de busca por texto completo.

---

## 📖 Sobre o Desenvolvimento

Durante este projeto aprofundei conhecimentos em Django REST Framework, organização de pastas, comandos customizados e deploy na nuvem.

Estou empolgada para:

Continuar evoluindo a API com novos recursos.

Aprender mais sobre performance e escalabilidade.

Compartilhar aprendizados com a comunidade dev.

---

## 🛠️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/usuario/flix_api.git
2. Acesse o diretório do projeto:
   ```bash
   cd flix_api
3. Crei e ative um ambiente virtual:
   ```bash
   python -m venv venv source venv/bin/activate # Para Windows: venv\Scripts\activate
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
5. Execute as migrações:
   ```bash
   python manage.py migrate
6. Inicie o servidor local:
   ```bash
   python manage.py runserver

