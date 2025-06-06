from app.repositories.alumno_repositorio import AlumnoRepository

class AlumnoService:
    
    @staticmethod
    def crear_alumno(alumno):
        """Crea un nuevo alumno"""
        return AlumnoRepository.crear_alumno(alumno)
    
    @staticmethod
    def buscar_todos():
        """Obtiene todos los alumnos"""
        return AlumnoRepository.buscar_todos()
    
    @staticmethod
    def buscar_alumno_id(alumno_id):
        """Obtiene un alumno por su ID"""
        return AlumnoRepository.buscar_alumno_id(alumno_id)
    
    @staticmethod
    def buscar_alumno_legajo(nro_legajo):
        """Obtiene un alumno por su número de legajo"""
        return AlumnoRepository.buscar_alumno_legajo(nro_legajo)
    
    @staticmethod
    def buscar_alumno_doc(nro_documento):
        """Obtiene un alumno por su número de documento"""
        return AlumnoRepository.buscar_alumno_documento(nro_documento)
    
    @staticmethod
    def actualizar_alumno(alumno):
        """Actualiza un alumno existente"""
        return AlumnoRepository.actualizar_alumno(alumno)
    
    @staticmethod
    def borrar_alumno_id(alumno_id):
        """Elimina un alumno por su ID"""
        return AlumnoRepository.borrar_alumno_id(alumno_id)