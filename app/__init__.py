from flask import Flask
from .config import Config
from .extensions import db, ma, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    from app import models
    ma.init_app(app)
    migrate.init_app(app, db)

    # Importar e registrar rotas aqui (exemplo com admin)
    from app.routes.admin_routes import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/api/admin')

    return app
