def registrar_blueprints(app):
    from app.resources import home_bp, universidad_bp, tipo_dedicacion_bp  # ,  certificado_bp
    app.register_blueprint(home_bp, url_prefix='/api/v1')
    app.register_blueprint(universidad_bp, url_prefix='/api/v1')
    # app.register_blueprint(certificado_bp, url_prefix= '/api/v1/certificado')
    app.register_blueprint(tipo_dedicacion_bp, url_prefix='/api/v1')