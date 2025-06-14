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
GET /api/admin

Retorna todos os administradores.

POST /api/admin

Cria um novo administrador.

Exemplo de JSON:
```json
{
  "username": "@teste",
	"email": "teste@gmail.com",
	"password": "teste123",
	"created_time": "2025-06-12 00:00:00"
}
```
Fluxo interno:

    O JSON é recebido pelo controller via request.get_json().

    Os dados são validados e desserializados pelo AdminSchema com admin_schema.load(data).

    O objeto Admin é persistido no banco via SQLAlchemy.

    A resposta é retornada com admin_schema.jsonify(admin).

GET /api/admin/<id_admin>

Retorna os dados de um administrador específico.

PUT /api/admin/<id_admin>

Atualiza os dados de um administrador.

Exemplo de JSON:

Supondo que executamos o exemplo de json na rota POST /api/admin para criar um novo administrador, e que esse seja o primeiro registro na base de dados, então receberá id_admin: 1 .
Vamos atualizar esse registro executando o seguinte endpoint:

PUT /api/admin/1

```json
{
  "username": "@admin",
	"email": "admin@gmail.com",
	"password": "admin@admin",
	"created_time": "2025-06-12 00:00:00"
}
```
Ao executar atualizamos o campo "password" de "admin123" para "admin@admin"

DELETE /api/admin/<id_admin>

Remove o administrador.
