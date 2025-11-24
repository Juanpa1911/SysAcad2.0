
from abc import ABC, abstractmethod
from typing import Dict, Any
from io import BytesIO


class FichaAlumnoExporter(ABC):
    """
    Interfaz base para exportadores de fichas de alumnos.
    Define el contrato que deben cumplir todos los exportadores.
    """
    
    @abstractmethod
    def export(self, ficha_data: Dict[str, Any]) -> Any:
        """
        Exporta los datos de la ficha a un formato específico.
        
        Args:
            ficha_data: Diccionario con los datos de la ficha del alumno
            
        Returns:
            Datos exportados en el formato específico
        """
        pass
    
    @abstractmethod
    def get_content_type(self) -> str:
        """
        Retorna el content-type HTTP apropiado para el formato.
        
        Returns:
            String con el content-type
        """
        pass


class JSONFichaExporter(FichaAlumnoExporter):
    """
    Exportador de fichas de alumnos en formato JSON.
    Responsabilidad única: Convertir datos a formato JSON.
    """
    
    def export(self, ficha_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Retorna los datos en formato JSON (diccionario Python).
        
        Args:
            ficha_data: Datos de la ficha
            
        Returns:
            Diccionario con los datos estructurados
        """
        return ficha_data
    
    def get_content_type(self) -> str:
        """Retorna el content-type para JSON"""
        return 'application/json'


class PDFFichaExporter(FichaAlumnoExporter):
    """
    Exportador de fichas de alumnos en formato PDF usando ReportLab.
    Responsabilidad única: Generar PDF nativo sin dependencias externas.
    No requiere GTK3 ni otras librerías del sistema operativo.
    """
    
    def export(self, ficha_data: Dict[str, Any]) -> bytes:
        """
        Genera un PDF a partir de los datos de la ficha usando ReportLab.
        
        Args:
            ficha_data: Datos de la ficha
            
        Returns:
            Bytes del PDF generado
        """
        from reportlab.lib.pagesizes import A4  # type: ignore
        from reportlab.lib.units import cm  # type: ignore
        from reportlab.lib import colors  # type: ignore
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer  # type: ignore
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # type: ignore
        from reportlab.lib.enums import TA_CENTER  # type: ignore
        
        # Crear buffer en memoria
        buffer = BytesIO()
        
        # Crear documento PDF
        doc = SimpleDocTemplate(buffer, pagesize=A4,
                                rightMargin=2*cm, leftMargin=2*cm,
                                topMargin=2*cm, bottomMargin=2*cm)
        
        # Contenedor de elementos (lista que acepta Flowables de ReportLab)
        elements: list = []  # type: ignore
        
        # Estilos
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=30,
            alignment=TA_CENTER
        )
        
        # Título
        title = Paragraph("<b>FICHA DEL ALUMNO</b>", title_style)
        elements.append(title)
        elements.append(Spacer(1, 0.5*cm))
        
        # Datos del alumno en tabla
        data = [
            ['Universidad:', ficha_data.get('universidad', 'Universidad Tecnológica Nacional')],
            ['Facultad:', ficha_data.get('facultad', 'San Rafael')],
            ['Nro. Legajo:', str(ficha_data.get('nro_legajo', 'N/A'))],
            ['Apellido y Nombre:', ficha_data.get('nombre_completo', 'N/A')],
            ['Tipo Documento:', ficha_data.get('tipo_documento', 'N/A')],
            ['Nro. Documento:', ficha_data.get('nro_documento', 'N/A')],
            ['Sexo:', ficha_data.get('sexo', 'N/A')],
            ['Fecha Nacimiento:', ficha_data.get('fecha_nacimiento', 'N/A')],
            ['Fecha Ingreso:', ficha_data.get('fecha_ingreso', 'N/A')],
        ]
        
        # Crear tabla
        table = Table(data, colWidths=[6*cm, 10*cm])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#3498db')),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 1*cm))
        
        # Fecha de emisión
        fecha_style = ParagraphStyle(
            'FechaStyle',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.grey,
            alignment=TA_CENTER
        )
        fecha = Paragraph(f"Fecha de emisión: {ficha_data.get('fecha_emision', 'N/A')}", fecha_style)
        elements.append(fecha)
        
        # Generar PDF
        doc.build(elements)
        
        # Obtener bytes
        pdf_bytes = buffer.getvalue()
        buffer.close()
        
        return pdf_bytes
    
    def get_content_type(self) -> str:
        """Retorna el content-type para PDF"""
        return 'application/pdf'


class FichaAlumnoExporterFactory:
    """
    Factory para crear exportadores según el formato solicitado.
    Facilita la extensión con nuevos formatos sin modificar código existente (Open/Closed).
    """
    
    _exporters = {
        'json': JSONFichaExporter,
        'pdf': PDFFichaExporter
    }
    
    @classmethod
    def create_exporter(cls, format_type: str) -> FichaAlumnoExporter:
        """
        Crea un exportador según el formato especificado.
        
        Args:
            format_type: Tipo de formato ('json' o 'pdf')
            
        Returns:
            Instancia del exportador correspondiente
            
        Raises:
            ValueError: Si el formato no es soportado
        """
        exporter_class = cls._exporters.get(format_type.lower())
        
        if not exporter_class:
            raise ValueError(f"Formato '{format_type}' no soportado. Formatos disponibles: {list(cls._exporters.keys())}")
        
        return exporter_class()
    
    @classmethod
    def register_exporter(cls, format_type: str, exporter_class: type):
        """
        Registra un nuevo tipo de exportador.
        Permite extender la funcionalidad sin modificar el código existente.
        
        Args:
            format_type: Identificador del formato
            exporter_class: Clase del exportador
        """
        cls._exporters[format_type.lower()] = exporter_class
