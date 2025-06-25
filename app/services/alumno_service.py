from app.repositories.alumno_repositorio import AlumnoRepository
from datetime import datetime
from io import BytesIO
import jinja2
from app.models import alumno
from flask import render_template, current_app, url_for
from weasyprint import HTML
from python_odt_template import ODTTemplate
from python_odt_template.jinja import get_odt_renderer
from docxtpl import DocxTemplate
import jinja2
import os


class AlumnoService:
    
    @staticmethod
    def crear_alumno(alumno):
        """
        Crea un nuevo alumno
        :param alumno: Objeto Alumno a crear.
        :return: Objeto Alumno creado.
        """
        return AlumnoRepository.crear_alumno(alumno)
    
    @staticmethod
    def buscar_todos():
        """
        Obtiene todos los alumnos
        :return: Lista de objetos Alumno.
        """
        return AlumnoRepository.buscar_todos()
    
    @staticmethod
    def buscar_alumno_id(alumno_id):
        """
        Obtiene un alumno por su ID
        :param alumno_id: ID del alumno a buscar.
        :return: Objeto Alumno encontrado o None si no se encuentra.
        """
        return AlumnoRepository.buscar_alumno_id(alumno_id)
    
    @staticmethod
    def buscar_alumno_legajo(nro_legajo):
        """
        Obtiene un alumno por su número de legajo
        :param nro_legajo: Número de legajo del alumno a buscar.
        :return: Objeto Alumno encontrado o None si no se encuentra.
        """
        return AlumnoRepository.buscar_alumno_legajo(nro_legajo)
    
    @staticmethod
    def buscar_alumno_doc(nro_documento):
        """
        Obtiene un alumno por su número de documento
        :param nro_documento: Número de documento del alumno a buscar.
        :return: Objeto Alumno encontrado o None si no se encuentra.
        """
        return AlumnoRepository.buscar_alumno_documento(nro_documento)
    
    @staticmethod
    def actualizar_alumno(alumno):
        """
        Actualiza un alumno existente
        :param alumno: Objeto Alumno con los nuevos datos.
        :return: Objeto Alumno actualizado o None si no se encuentra.
        """
        return AlumnoRepository.actualizar_alumno(alumno)
    
    @staticmethod
    def borrar_alumno_id(alumno_id):
<<<<<<< Updated upstream
        """
        Elimina un alumno por su ID
        :param alumno_id: ID del alumno a eliminar.
        :return: Objeto Alumno eliminado o None si no se encuentra.
        """
        return AlumnoRepository.borrar_alumno_id(alumno_id)
=======
        """Elimina un alumno por su ID"""
        return AlumnoRepository.borrar_alumno_id(alumno_id)
    
    def generar_certificado_alumno_regular(id: int):
        """Genera un certificado de alumno regular"""
        alumno = AlumnoRepository.buscar_alumno_id(id)
        if not alumno:
            return None
        
        fecha_actual = datetime.datetime.now()
        fecha_str = fecha_actual.strftime('%d de %B de %Y')
        #TODO: relacionar alumno con facultad y especialidad 
        especialidad = alumno.especialidad
        facultad = especialidad.facultad
        universidad = facultad.universidad
        html_string = render_template('certificado/certificado_pdf.html', alumno=alumno,
                                    facultad=facultad,
                                    especialidad=especialidad,
                                    universidad=universidad,
                                    fecha=fecha_str)
        base_url = url_for('static', filename='', _external=True)
        bytes_data = HTML(string=html_string, base_url=base_url).write_pdf()
        pdf_io = BytesIO(bytes_data)
        return pdf_io

    @staticmethod
    def generar_certificado_alumno_regular_odt(id: int):
        alumno = AlumnoRepository.buscar_por_id(id)
        if not alumno:
            return None

        fecha_actual = datetime.datetime.now()
        fecha_str = fecha_actual.strftime('%d de %B de %Y')
        especialidad = alumno.especialidad
        facultad = especialidad.facultad
        universidad = facultad.universidad
        
        odt_renderer = get_odt_renderer(media_path=url_for('static', filename='media'))
        path_template = os.path.join(current_app.root_path, 'templates', 'certificado', 'certificado_plantilla.odt')
        
        
        odt_io = BytesIO()
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.odt', delete=False) as temp_file:
            temp_path = temp_file.name

        with ODTTemplate(path_template) as template:
            odt_renderer.render( template,
                context={
                        "alumno":alumno, 
                        "facultad": facultad, 
                        "especialidad": especialidad, 
                        "universidad": universidad, 
                        "fecha": fecha_str
                        }
            )
            template.pack(temp_path)
            with open(temp_path, 'rb') as f:
                odt_io.write(f.read())
            
        os.unlink(temp_path)
        odt_io.seek(0)
        return odt_io
    
    @staticmethod
    def generar_certificado_alumno_regular_docx(id: int):
        alumno = AlumnoRepository.buscar_por_id(id)
        if not alumno:
            return None
        fecha_actual = datetime.datetime.now()
        fecha_str = fecha_actual.strftime('%d de %B de %Y')
        especialidad = alumno.especialidad
        facultad = especialidad.facultad
        universidad = facultad.universidad
        path_template = os.path.join(current_app.root_path, 'templates', 'certificado', 'certificado_plantilla.docx')
        doc = DocxTemplate(path_template)
        
        docx_io = BytesIO()
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.odt', delete=False) as temp_file:
            temp_path = temp_file.name

        context={
                "alumno":alumno, 
                "facultad": facultad, 
                "especialidad": especialidad, 
                "universidad": universidad, 
                "fecha": fecha_str
                }
        jinja_env = jinja2.Environment()
    
        doc.render(context, jinja_env)
        doc.save(temp_path)
        with open(temp_path, 'rb') as f:
                docx_io.write(f.read())
            
        os.unlink(temp_path)
        docx_io.seek(0)
        return docx_io
>>>>>>> Stashed changes
