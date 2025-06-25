from app.repositories.alumno_repositorio import AlumnoRepository

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
        """
        Elimina un alumno por su ID
        :param alumno_id: ID del alumno a eliminar.
        :return: Objeto Alumno eliminado o None si no se encuentra.
        """
        return AlumnoRepository.borrar_alumno_id(alumno_id)