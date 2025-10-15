def registrar_blueprints(app):
    from app.resources import home_bp, universidad_bp, area_bp, cargo_bp, alumno_bp, tipo_dedicacion_bp, departamento_bp, especialidad_bp  # ,  certificado_bp
    app.register_blueprint(home_bp, url_prefix='/api/v1')
    app.register_blueprint(universidad_bp, url_prefix='/api/v1')
    app.register_blueprint(area_bp, url_prefix='/api/v1')
    app.register_blueprint(cargo_bp, url_prefix='/api/v1')
    app.register_blueprint(alumno_bp, url_prefix='/api/v1')
    app.register_blueprint(tipo_dedicacion_bp, url_prefix='/api/v1')
    app.register_blueprint(departamento_bp, url_prefix='/api/v1')
    app.register_blueprint(especialidad_bp, url_prefix='/api/v1')