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
```

No arquivo ".env" altere o conteúdo das variáveis de ambiente de acordo com as credenciais da sua base de dados:
```python
DB_HOST=localhost
DB_PORT=3306 padrão do mysql ou outra porta que você definiu
DB_NAME=nome da base
DB_USER=usuário
DB_PASSWORD=senha

```
## 📌 Endpoints principais
🔹 Admin
GET /admin

Retorna todos os administradores.
POST /admin

Cria um novo administrador.

Exemplo de JSON:
```json
{
  "name": "Ana Silva",
  "email": "ana@exemplo.com"
}
```
Fluxo interno:

    O JSON é recebido pelo controller via request.get_json().

    Os dados são validados e desserializados pelo AdminSchema com admin_schema.load(data).

    O objeto Admin é persistido no banco via SQLAlchemy.

    A resposta é retornada com admin_schema.jsonify(admin).

GET /admin/<id>

Retorna os dados de um administrador específico.
PUT /admin/<id>

Atualiza os dados de um administrador.

Exemplo de JSON:
```json
{
  "name": "Ana Paula",
  "email": "ana.paula@exemplo.com"
}
```
DELETE /admin/<id>

Remove o administrador.
