
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
        Incluye logos institucionales y diseño profesional con colores UTN.
        
        Args:
            ficha_data: Datos de la ficha
            
        Returns:
            Bytes del PDF generado
        """
        from reportlab.lib.pagesizes import A4  # type: ignore
        from reportlab.lib.units import cm  # type: ignore
        from reportlab.lib import colors  # type: ignore
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable, Image  # type: ignore
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # type: ignore
        from reportlab.lib.enums import TA_CENTER, TA_LEFT  # type: ignore
        import os
        
        # Crear buffer en memoria
        buffer = BytesIO()
        
        # Crear documento PDF
        doc = SimpleDocTemplate(buffer, pagesize=A4,
                                rightMargin=2*cm, leftMargin=2*cm,
                                topMargin=1.5*cm, bottomMargin=1.5*cm)
        
        # Contenedor de elementos
        elements: list = []  # type: ignore
        
        # Estilos
        styles = getSampleStyleSheet()
        
        # Colores institucionales UTN
        color_utn_azul = colors.HexColor('#003D7A')  # Azul UTN
        color_utn_celeste = colors.HexColor('#0099CC')  # Celeste UTN
        color_gris_claro = colors.HexColor('#F5F5F5')
        
        # === ENCABEZADO CON LOGO ===
        try:
            # Intentar cargar el logo de la UTN
            logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'img', 'logo-utn.png')
            if os.path.exists(logo_path):
                logo = Image(logo_path, width=3*cm, height=3*cm)
                logo.hAlign = 'CENTER'
                elements.append(logo)
                elements.append(Spacer(1, 0.3*cm))
        except Exception:
            pass  # Si no se puede cargar el logo, continuar sin él
        
        # Estilos de encabezado
        header_style = ParagraphStyle(
            'HeaderStyle',
            parent=styles['Normal'],
            fontSize=11,
            textColor=color_utn_azul,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            spaceAfter=3
        )
        
        subheader_style = ParagraphStyle(
            'SubHeaderStyle',
            parent=styles['Normal'],
            fontSize=9,
            textColor=color_utn_azul,
            alignment=TA_CENTER,
            spaceAfter=5
        )
        
        # Encabezado institucional
        universidad = Paragraph(ficha_data.get('universidad', 'Universidad Tecnológica Nacional'), header_style)
        facultad = Paragraph(ficha_data.get('facultad', 'Facultad Regional'), subheader_style)
        elements.append(universidad)
        elements.append(facultad)
        
        # Línea divisoria decorativa
        elements.append(HRFlowable(width="100%", thickness=3, color=color_utn_azul, spaceBefore=8, spaceAfter=5))
        elements.append(HRFlowable(width="100%", thickness=1, color=color_utn_celeste, spaceBefore=2, spaceAfter=15))
        
        # === TÍTULO PRINCIPAL ===
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor=color_utn_azul,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            spaceAfter=20
        )
        
        title = Paragraph("FICHA DEL ALUMNO", title_style)
        elements.append(title)
        
        # === SECCIÓN: DATOS PERSONALES ===
        section_style = ParagraphStyle(
            'SectionStyle',
            parent=styles['Normal'],
            fontSize=12,
            textColor=colors.white,
            alignment=TA_LEFT,
            fontName='Helvetica-Bold',
            leftIndent=10,
            spaceBefore=10,
            spaceAfter=8
        )
        
        # Crear encabezado de sección como tabla para fondo de color
        section_personal = Table([['📋  DATOS PERSONALES']], colWidths=[16*cm])
        section_personal.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color_utn_azul),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 15),
        ]))
        elements.append(section_personal)
        
        # Tabla de datos personales
        data_personal = [
            ['Nro. Legajo:', str(ficha_data.get('nro_legajo', 'N/A'))],
            ['Apellido y Nombre:', ficha_data.get('nombre_completo', 'N/A')],
            ['Tipo de Documento:', ficha_data.get('tipo_documento', 'N/A')],
            ['Nro. de Documento:', ficha_data.get('nro_documento', 'N/A')],
            ['Sexo:', ficha_data.get('sexo', 'N/A')],
            ['Fecha de Nacimiento:', ficha_data.get('fecha_nacimiento', 'N/A')],
        ]
        
        table_personal = Table(data_personal, colWidths=[5.5*cm, 10.5*cm])
        table_personal.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), color_utn_celeste),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
            ('BACKGROUND', (1, 0), (1, -1), color_gris_claro),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('LEFTPADDING', (0, 0), (-1, -1), 15),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        elements.append(table_personal)
        elements.append(Spacer(1, 0.6*cm))
        
        # === SECCIÓN: DATOS ACADÉMICOS ===
        section_academico = Table([['🎓  DATOS ACADÉMICOS']], colWidths=[16*cm])
        section_academico.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color_utn_azul),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 15),
        ]))
        elements.append(section_academico)
        
        # Tabla de datos académicos
        data_academico = [
            ['Fecha de Ingreso:', ficha_data.get('fecha_ingreso', 'N/A')],
            ['Facultad:', ficha_data.get('facultad', 'N/A')],
            ['Universidad:', ficha_data.get('universidad', 'N/A')],
        ]
        
        table_academico = Table(data_academico, colWidths=[5.5*cm, 10.5*cm])
        table_academico.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), color_utn_celeste),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
            ('BACKGROUND', (1, 0), (1, -1), color_gris_claro),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('LEFTPADDING', (0, 0), (-1, -1), 15),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        elements.append(table_academico)
        elements.append(Spacer(1, 1.2*cm))
        
        # === PIE DE PÁGINA ===
        elements.append(HRFlowable(width="100%", thickness=1, color=color_utn_celeste, spaceBefore=5, spaceAfter=8))
        
        footer_style = ParagraphStyle(
            'FooterStyle',
            parent=styles['Normal'],
            fontSize=8,
            textColor=colors.grey,
            alignment=TA_CENTER,
            fontName='Helvetica-Oblique'
        )
        
        footer = Paragraph(f"<i>Documento generado electrónicamente el {ficha_data.get('fecha_emision', 'N/A')}</i>", footer_style)
        elements.append(footer)
        
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
