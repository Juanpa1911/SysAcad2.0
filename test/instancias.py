from _pydatetime import datetime
from datetime import date
from app.models import (
    Alumno, Area, Autoridad, Cargo, CategoriaCargo, Departamento,
    Especialidad, Facultad, Grado, Grupo, Materia, Orientacion,
    Plan, TipoDedicacion, TipoDocumento, TipoEspecialidad, Universidad
)

from app.services import (
    AlumnoService, AreaService,AutoridadService, CargoService, CategoriaCargoService,
    DepartamentoService, EspecialidadService, FacultadService, GradoService, GrupoService,
    MateriaService, OrientacionService, PlanService, TipoDedicacionService,
    TipoEspecialidadService, UniversidadService
)
from app.services.tipo_doc_service import TipoDocumentoService

def nuevaUniversidad(nombre="Universidad Nacional de La Plata", sigla="UNLP"):
    universidad=Universidad()
    universidad.nombre = nombre
    universidad.sigla = sigla
    UniversidadService.crear_universidad(universidad)
    return universidad

def nuevaFacultad(nombre="Facultad de Ingeniería", abreviatura="FI", universidad_id=1):
    facultad = Facultad()
    facultad.nombre = nombre
    facultad.abreviatura = abreviatura
    facultad.directorio = "Directorio de la Facultad"
    facultad.sigla = abreviatura
    facultad.codigo_postal = "1900"
    facultad.ciudad = "La Plata"
    facultad.domicilio = "Calle 1 y 47"
    facultad.telefono = "0221-421-7578"
    facultad.contacto = f"contacto@{abreviatura.lower()}.unlp.edu.ar"
    facultad.email = f"info@{abreviatura.lower()}.unlp.edu.ar"
    facultad.universidad_id = universidad_id
    FacultadService.crear_facultad(facultad)
    return facultad

def nuevoDepartamento(nombre="Departamento de Sistemas", descripcion="Departamento de estudiantes de ingeniería en sistemas"):
    departamento = Departamento()
    departamento.nombre = nombre
    departamento.descripcion = descripcion
    DepartamentoService.crear_departamento(departamento)
    return departamento

def nuevoCargo(nombre = "Decano", puntos = 100, categoria_cargo = None, tipo_dedicacion = None):
    cargo = Cargo()
    cargo.nombre = nombre
    cargo.puntos = puntos
    cargo.categoria_cargo = nuevaCategoriaCargo() 
    cargo.tipo_dedicacion = nuevoTipoDedicacion() 
    CargoService.crear_cargo(cargo)
    return cargo

def nuevaCategoriaCargo(nombre="Categoría A"):
    categoria = CategoriaCargo()
    categoria.nombre = nombre
    CategoriaCargoService.crear_categoria_cargo(categoria)
    return categoria

def nuevoTipoDedicacion(nombre="Tiempo Completo", observacion="Dedicación a tiempo completo"):
    tipo = TipoDedicacion()
    tipo.nombre = nombre
    tipo.observacion = observacion      
    TipoDedicacionService.crear_tipo_dedicacion(tipo)
    return tipo

def nuevaArea(nombre="Área de Investigación"):
    area = Area()
    area.nombre = nombre
    AreaService.crear_area(area)
    return area

def nuevaEspecialidad(nombre="Ingeniería en Sistemas", letra="IS", observacion="Especialidad de Ingeniería en Sistemas", departamento=None):
    especialidad = Especialidad()
    especialidad.nombre = nombre
    especialidad.letra = letra
    especialidad.observacion = observacion
    EspecialidadService.crear_especialidad(especialidad)
    return especialidad

def nuevaAutoridad(nombre="Juan Pérez", telefono="123456789", email="juan.perez@unlp.edu.ar"):
    autoridad = Autoridad()
    autoridad.nombre = nombre
    autoridad.telefono = telefono
    autoridad.email = email
    AutoridadService.crear_autoridad(autoridad)
    return autoridad

def nuevoGrado(nombre="Licenciatura"):
    grado = Grado()
    grado.nombre = nombre
    GradoService.crear_grado(grado)
    return grado

def nuevoGrupo(nombre="Grupo A"):
    grupo = Grupo()
    grupo.nombre = nombre
    GrupoService.crear_grupo(grupo)
    return grupo

def nuevaMateria(nombre="Análisis Matemático I", codigo="ANMAT1", observacion="Introducción al Análisis Matemático", orientacion=None, autoridad=None):
    materia = Materia()
    materia.nombre = nombre
    materia.codigo = codigo
    materia.observacion = observacion
    MateriaService.crear_materia(materia)
    materia.orientacion = nuevaOrientacion()
    materia.autoridades = [nuevaAutoridad("Dr. Carlos Gómez", "987 654321", "dr.carlos.gomez@unlp.edu.ar")]
    return materia

def nuevaOrientacion(nombre="Sistemas de Información"):
    orientacion = Orientacion()
    orientacion.nombre = nombre
    OrientacionService.crear_orientacion(orientacion)
    return orientacion

def nuevoPlan(nombre="Plan 2023", observacion="Plan de estudios 2023", fecha_inicio=date(2023, 1, 1), fecha_fin=date(2028, 12, 31)):
    plan = Plan()
    plan.nombre = nombre
    plan.observacion = observacion
    plan.fecha_inicio = fecha_inicio
    plan.fecha_fin = fecha_fin
    PlanService.crear_plan(plan)
    return plan

def nuevaTipoDedicacion(nombre="Parcial", observacion="Dedicacion parcial"):
    tipo = TipoDedicacion()
    tipo.nombre = nombre
    tipo.observacion = observacion      
    TipoDedicacionService.crear_tipo_dedicacion(tipo)
    return tipo

def nuevoTipoDocumento(nombre="DNI"):
    tipo_doc = TipoDocumento()
    tipo_doc.nombre = nombre
    TipoDocumentoService.crear_tipo_documento(tipo_doc)
    return tipo_doc

def nuevoTipoEspecialidad(nombre="Técnica", nivel="Básico"):
    tipo_esp = TipoEspecialidad()
    tipo_esp.nombre = nombre
    tipo_esp.nivel = nivel
    TipoEspecialidadService.crear_tipo_especialidad(tipo_esp)
    return tipo_esp

def nuevoAlumno(apellido="Pérez", nombre="Juan", nro_documento="30123456", tipo_documento=None, fecha_nacimiento="1990-01-15", sexo="M", nro_legajo=12345, fecha_ingreso=date.today()):
    alumno = Alumno()
    alumno.apellido = apellido
    alumno.nombre = nombre
    alumno.nro_documento = nro_documento
    alumno.tipo_documento = nuevoTipoDocumento()
    alumno.fecha_nacimiento = fecha_nacimiento
    alumno.sexo = sexo
    alumno.nro_legajo = nro_legajo
    alumno.fecha_ingreso = fecha_ingreso
    return alumno
