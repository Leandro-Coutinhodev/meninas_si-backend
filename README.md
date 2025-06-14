# 📦 Meninas SI - Backend API

API desenvolvida com **Flask** e **MySQL** para gerenciamento de:
- Administradores
- Membros
- Eventos
- Workshops
- Cursos de curta duração

Serialização feita com **Marshmallow**, arquitetura separada por camadas (controllers, services, models, schemas).

---

## 🚀 Tecnologias
- Python 3.13
- Flask
- SQLAlchemy
- Marshmallow
- MySQL

---

## 🔧 Instalação

```bash
# Clone o repositório
$ git clone https://github.com/Leandro-Coutinhodev/meninas_si-backend.git

# Acesse o diretório
$ cd meninas_si-backend

# Crie um ambiente virtual
$ python -m venv venv
$ source venv/bin/activate  # Linux/macOS
# ou
$ venv\Scripts\activate  # Windows

# Instale as dependências
$ pip install -r requirements.txt

# Execute a API
$ python run.py
