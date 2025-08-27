from app.repositories import AlumnoRepository
from datetime import datetime
from io import BytesIO
import jinja2
from flask import render_template, current_app, url_for
from typing import Optional


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
    def obtener_ficha_alumno_por_id(id: int) -> Optional[Alumno]:
        return AlumnoRepository.buscar_con_facultad(id)
    
    @staticmethod
    def obtener_ficha_alumno_por_legajo(legajo: str) -> Optional[Alumno]:
        return AlumnoRepository.buscar_por_legajo_con_facultad(legajo)
    
    