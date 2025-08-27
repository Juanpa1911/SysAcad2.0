from abc import ABC, abstractmethod
from typing import Dict, Any
from app.models import Alumno

class DocumentoGeneratorInterface(ABC):
    @abstractmethod
    def generar(self, alumno: Alumno) -> Any:
        pass

class PDFGeneratorService(DocumentoGeneratorInterface):
    def generar(self, alumno: Alumno) -> bytes:
        from weasyprint import HTML, CSS
        
        html_content = self._generar_html_ficha(alumno)
        css_content = self._obtener_estilos()
        
        pdf = HTML(string=html_content).write_pdf(stylesheets=[CSS(string=css_content)])
        return pdf
    
    def _generar_html_ficha(self, alumno: Alumno) -> str:
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Ficha del Alumno</title>
        </head>
        <body>
            <div class="ficha-alumno">
                <h1>Ficha del Alumno</h1>
                <div class="datos">
                    <p><strong>Legajo:</strong> {alumno.nro_legajo}</p>
                    <p><strong>Apellido y Nombre:</strong> {alumno.apellido}, {alumno.nombre}</p>
                    <p><strong>Número documento:</strong> {alumno.nro_documento}<p/>
                    <p><strong>Facultad:</strong> {alumno.facultad.nombre if alumno.facultad else 'No asignada'}</p>
                    <p><strong>Abreviatura:</strong> {alumno.facultad.abreviatura if alumno.facultad else 'N/A'}</p>
                </div>
            </div>
        </body>
        </html>
        """
    
    def _obtener_estilos(self) -> str:
        """CSS para el PDF"""
        return """
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        .ficha-alumno {
            border: 2px solid #333;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            color: #333;
            text-align: center;
            border-bottom: 2px solid #ccc;
            padding-bottom: 10px;
        }
        .datos p {
            margin: 10px 0;
            font-size: 14px;
        }
        """

class FichaAlumnoService:
    def __init__(self, pdf_generator: DocumentoGeneratorInterface = None):
        self.pdf_generator = pdf_generator or PDFGeneratorService()
    
    def generar_ficha_pdf(self, alumno: Alumno) -> bytes:
        return self.pdf_generator.generar(alumno)