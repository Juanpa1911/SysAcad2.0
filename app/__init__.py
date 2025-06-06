import logging
from flask import Flask
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')
    #https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from app.resources import home
    app.register_blueprint(home, url_prefix= '/api/v1')
    from app.resources import universidad_bp
    app.register_blueprint(universidad_bp, url_prefix='/api/v1/universidad')

    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
