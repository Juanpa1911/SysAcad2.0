from app.repositories import AlumnoRepository
from datetime import datetime
from io import BytesIO
import jinja2
from flask import render_template, current_app, url_for
from typing import Dict, Any, Optional


class AlumnoService:
    
    @staticmethod
    def crear_alumno(alumno):
        return AlumnoRepository.crear_alumno(alumno)
    
    @staticmethod
    def buscar_todos():
        return AlumnoRepository.buscar_todos()
    
    @staticmethod
    def buscar_alumno_id(alumno_id):
        return AlumnoRepository.buscar_alumno_id(alumno_id)
    
    @staticmethod
    def buscar_alumno_legajo(nro_legajo):
        return AlumnoRepository.buscar_alumno_legajo(nro_legajo)
    
    @staticmethod
    def buscar_alumno_doc(nro_documento):
        return AlumnoRepository.buscar_alumno_documento(nro_documento)
    
    @staticmethod
    def actualizar_alumno(alumno):
        return AlumnoRepository.actualizar_alumno(alumno)
    
    @staticmethod
    def borrar_alumno_id(alumno_id):
        return AlumnoRepository.borrar_alumno_id(alumno_id)
    
    @staticmethod
    def obtener_datos_ficha(alumno_id) -> Optional[Dict[str, Any]]:
        """
        Obtiene los datos del alumno formateados para la ficha.
        Responsabilidad única: transformar datos del modelo a formato de ficha.
        
        Args:
            alumno_id: ID del alumno
            
        Returns:
            Diccionario con los datos de la ficha o None si no existe
        """
        alumno = AlumnoRepository.obtener_ficha_completa(alumno_id)
        
        if not alumno:
            return None
        
        # Formatear los datos para la ficha
        ficha_data = {
            'nro_legajo': alumno.nro_legajo,
            'apellido': alumno.apellido,
            'nombre': alumno.nombre,
            'nombre_completo': f"{alumno.apellido}, {alumno.nombre}",
            'tipo_documento': alumno.tipo_documento.nombre if alumno.tipo_documento else 'N/A',
            'nro_documento': alumno.nro_documento,
            'fecha_nacimiento': alumno.fecha_nacimiento,
            'sexo': 'Masculino' if alumno.sexo == 'M' else 'Femenino' if alumno.sexo == 'F' else 'Otro',
            'fecha_ingreso': alumno.fecha_ingreso.strftime('%d/%m/%Y') if alumno.fecha_ingreso else 'N/A',
            'fecha_emision': datetime.now().strftime('%d/%m/%Y %H:%M'),
            'facultad': alumno.facultad.nombre if alumno.facultad else 'Sin asignar',
            'facultad_abreviatura': alumno.facultad.abreviatura if alumno.facultad else 'N/A',
            'universidad': alumno.facultad.universidad.nombre if alumno.facultad and alumno.facultad.universidad else 'Sin asignar',
            'universidad_sigla': alumno.facultad.universidad.sigla if alumno.facultad and alumno.facultad.universidad else 'N/A',
        }
        
        return ficha_data