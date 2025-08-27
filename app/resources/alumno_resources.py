from flask import Blueprint, jsonify, make_response, request
from app.services.alumno_service import AlumnoService
from app.services.documento_service import FichaAlumnoService
from app.mapping.alumno_mapping import AlumnoFichaMapping

alumno_bp = Blueprint('alumno', __name__)
alumno_ficha_mapping = AlumnoFichaMapping()
ficha_service = FichaAlumnoService()

@alumno_bp.route('/alumno/<int:id>/ficha', methods=['GET'])
def obtener_ficha_alumno(id: int):
    try:
        alumno = AlumnoService.obtener_ficha_alumno_por_id(id)
        if not alumno:
            return {'error': 'Alumno no encontrado'}, 404
        
        ficha_data = alumno_ficha_mapping.dump(alumno)
        return jsonify(ficha_data), 200
    
    except Exception as e:
        return {'error': str(e)}, 500

@alumno_bp.route('/alumno/<int:id>/ficha/pdf', methods=['GET'])
def obtener_ficha_alumno_pdf(id: int):
    try:
        alumno = AlumnoService.obtener_ficha_alumno_por_id(id)
        if not alumno:
            return {'error': 'Alumno no encontrado'}, 404
        
        pdf_content = ficha_service.generar_ficha_pdf(alumno)
        
        response = make_response(pdf_content)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=ficha_alumno_{alumno.legajo}.pdf'
        
        return response
    
    except Exception as e:
        return {'error': str(e)}, 500

@alumno_bp.route('/alumno/legajo/<string:legajo>/ficha', methods=['GET'])
def obtener_ficha_por_legajo(legajo: str):
    try:
        alumno = AlumnoService.obtener_ficha_alumno_por_legajo(legajo)
        if not alumno:
            return {'error': 'Alumno no encontrado'}, 404
        
        ficha_data = alumno_ficha_mapping.dump(alumno)
        return jsonify(ficha_data), 200
    
    except Exception as e:
        return {'error': str(e)}, 500

@alumno_bp.route('/alumno/legajo/<string:legajo>/ficha/pdf', methods=['GET'])
def obtener_ficha_por_legajo_pdf(legajo: str):
    try:
        alumno = AlumnoService.obtener_ficha_alumno_por_legajo(legajo)
        if not alumno:
            return {'error': 'Alumno no encontrado'}, 404
        
        pdf_content = ficha_service.generar_ficha_pdf(alumno)
        
        response = make_response(pdf_content)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=ficha_alumno_{alumno.legajo}.pdf'
        
        return response
    
    except Exception as e:
        return {'error': str(e)}, 500