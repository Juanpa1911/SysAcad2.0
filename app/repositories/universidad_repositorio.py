from app import db
from app.models.universidad import Universidad

class UniversidadRepository:
    """
    Clase de repositorio para la entidad Universidad.
    """
    @staticmethod
    def crear_universidad(universidad):
        """
        Crea una nueva universidad en la base de datos.
        :param universidad: Objeto Universidad a crear.
        :return: Objeto Universidad creado.
        """
        db.session.add(universidad)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una universidad por su ID.
        :param id: ID de la universidad a buscar.
        :return: Objeto Universidad encontrado o None si no se encuentra.
        """
        return db.session.query(Universidad).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        """
        Busca todas las universidades en la base de datos.
        :return: Lista de objetos Universidad.
        """
        return db.session.query(Universidad).all()

    @staticmethod
    def actualizar_universidad(universidad) -> Universidad:
        """
        Actualiza una universidad existente en la base de datos.
        :param id: ID de la universidad a actualizar.
        :param universidad: Objeto Universidad con los nuevos datos.
        :return: Objeto Universidad actualizado o None si no se encuentra.
        """
        universidad_existente = db.session.merge(universidad)
        if not universidad_existente:
            return None
        return universidad_existente

    @staticmethod
    def borrar_universidad(id: int) -> Universidad:
        """
        Borra una universidad por su ID.
        :param id: ID de la universidad a borrar.
        :return: True si se borró correctamente, False si no se encontró.
        """
        universidad = db.session.query(Universidad).filter_by(id=id).first()
        if not universidad:
            return None
        db.session.delete(universidad)
        db.session.commit()
        return False