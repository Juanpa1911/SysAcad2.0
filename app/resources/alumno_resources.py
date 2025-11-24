from flask import jsonify, Blueprint, request, Response, send_file
from app.services import AlumnoService
from app.mapping.alumno_mapping import AlumnoMapping
from app.services.ficha_alumno_exporter import FichaAlumnoExporterFactory
from io import BytesIO

alumno_bp = Blueprint('alumno', __name__)
alumno_mapping = AlumnoMapping()

@alumno_bp.route('/alumno', methods=['GET'])
def buscar_todos():
    alumnos = AlumnoService.buscar_todos()
    return alumno_mapping.dump(alumnos, many=True), 200

@alumno_bp.route('/alumno/<hashid:id>', methods=['GET'])
def buscar_alumno_id(id):
    alumno = AlumnoService.buscar_alumno_id(id)
    if alumno:
        return alumno_mapping.dump(alumno), 200
    return jsonify({"message": "Alumno no encontrado"}), 404

@alumno_bp.route('/alumno/legajo/<int:nro_legajo>', methods=['GET'])
def buscar_alumno_legajo(nro_legajo):
    alumno = AlumnoService.buscar_alumno_legajo(nro_legajo)
    if alumno:
        return alumno_mapping.dump(alumno), 200
    return jsonify({"message": "Alumno no encontrado"}), 404

@alumno_bp.route('/alumno/documento/<string:nro_documento>', methods=['GET'])
def buscar_alumno_doc(nro_documento):
    alumno = AlumnoService.buscar_alumno_doc(nro_documento)
    if alumno:
        return alumno_mapping.dump(alumno), 200
    return jsonify({"message": "Alumno no encontrado"}), 404

@alumno_bp.route('/alumno', methods=['POST'])
def crear_alumno():
    data = request.get_json()
    alumno = alumno_mapping.load(data)
    AlumnoService.crear_alumno(alumno)
    return alumno_mapping.dump(alumno), 201

@alumno_bp.route('/alumno/<hashid:id>', methods=['PUT'])
def actualizar_alumno(id):
    data = request.get_json()
    alumno = alumno_mapping.load(data)
    AlumnoService.actualizar_alumno(alumno)
    if alumno:
        return alumno_mapping.dump(alumno), 200
    return jsonify({"message": "Alumno no encontrado"}), 404

@alumno_bp.route('/alumno/<hashid:id>', methods=['DELETE'])
def eliminar_alumno(id):
    alumno = AlumnoService.borrar_alumno_id(id)
    if alumno:
        return jsonify({"message": "Alumno eliminado"}), 200
    return jsonify({"message": "Alumno no encontrado"}), 404   


@alumno_bp.route('/alumno/<hashid:id>/ficha', methods=['GET'])
def obtener_ficha_alumno(id):
    """
    Endpoint para obtener la ficha del alumno en formato JSON o PDF.
    
    Query parameters:
        format: 'json' (default) o 'pdf'
    
    Ejemplos:
        GET /alumno/{id}/ficha?format=json
        GET /alumno/{id}/ficha?format=pdf
    """
    # Obtener el formato solicitado (por defecto JSON)
    format_type = request.args.get('format', 'json').lower()
    
    # Validar formato
    if format_type not in ['json', 'pdf']:
        return jsonify({
            "message": "Formato no válido",
            "error": f"El formato '{format_type}' no es soportado. Use 'json' o 'pdf'"
        }), 400
    
    # Obtener datos de la ficha
    ficha_data = AlumnoService.obtener_datos_ficha(id)
    
    if not ficha_data:
        return jsonify({"message": "Alumno no encontrado"}), 404
    
    try:
        # Crear el exportador usando el Factory (Open/Closed principle)
        exporter = FichaAlumnoExporterFactory.create_exporter(format_type)
        
        # Exportar los datos
        exported_data = exporter.export(ficha_data)
        
        # Responder según el formato
        if format_type == 'json':
            return jsonify(exported_data), 200
        else:  # pdf
            # Crear respuesta con el PDF
            pdf_buffer = BytesIO(exported_data)
            pdf_buffer.seek(0)
            
            filename = f"ficha_alumno_{ficha_data['nro_legajo']}.pdf"
            
            return send_file(
                pdf_buffer,
                mimetype=exporter.get_content_type(),
                as_attachment=True,
                download_name=filename
            )
            
    except ValueError as e:
        return jsonify({
            "message": "Error al generar la ficha",
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "message": "Error interno al generar la ficha",
            "error": str(e)
        }), 500


@alumno_bp.route('/alumno/legajo/<int:nro_legajo>/ficha', methods=['GET'])
def obtener_ficha_alumno_por_legajo(nro_legajo):
    """
    Endpoint para obtener la ficha del alumno por número de legajo.
    
    Query parameters:
        format: 'json' (default) o 'pdf'
    
    Ejemplos:
        GET /alumno/legajo/12345/ficha?format=json
        GET /alumno/legajo/12345/ficha?format=pdf
    """
    # Buscar el alumno por legajo
    alumno = AlumnoService.buscar_alumno_legajo(nro_legajo)
    
    if not alumno:
        return jsonify({"message": "Alumno no encontrado"}), 404
    
    # Delegar al endpoint principal usando el ID
    return obtener_ficha_alumno(alumno.id)
