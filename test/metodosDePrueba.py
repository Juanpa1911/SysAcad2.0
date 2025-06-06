from app.models import * 
from app.services import *


# metodo para crear un nuevo departamento y no repetir tanto codigo
def nuevoDepartamento():
    departamento = Departamento()
    departamento.nombre = "ofina de alumnos"
    departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
    return departamento
    
def nuevoDepartamento2():
    departamento = Departamento()
    departamento.nombre = "ofina de profesores"
    departamento.descripcion = "oficina de profesores de la facultad de ingenieria"
    return departamento



def nuevoOrientacion():
    orientacion = Orientacion()
    orientacion.nombre = "Orientacion1"
    return orientacion 
   
def nuevoOrientacion2():
    orientacion = Orientacion()
    orientacion.nombre = "Orientacion2"
    return orientacion    
# metodos para crear objetos de prueba

def nuevoMateria():
    materia = Materia()
    materia.nombre = "Matematica"
    materia.codigo = "MAT101"
    materia.observacion = "Matematica basica"
    materia.asociar_autoridad(nuevaAutoridad())
    materia.orientacion = nuevoOrientacion()
    return materia

def nuevaMateria2():
    materia = Materia()
    materia.nombre = "Base de datos"
    materia.codigo = "BD101"
    materia.observacion = "Base de datos basica"
    materia.orientacion = nuevoOrientacion2()
    return materia

def nuevaAutoridad():
    autoridad = Autoridad()
    autoridad.nombre = "Juan Perez"
    autoridad.telefono = "123456789"
    autoridad.email = "email123@mail.com"
    autoridad.cargo = nuevoCargo()
    return autoridad
    
def nuevoCargo():
    cargo = Cargo()
    cargo.nombre = "Profesor"
    cargo.puntos = 10
    cargo.categoria_cargo = categoriaCargo()
    cargo.tipo_dedicacion = tipoDeCargo()
    return cargo

def tipoDeCargo():
    tipo = TipoDedicacion()
    tipo.nombre = "Tiempo completo"
    return tipo
        
def categoriaCargo():
    categoria = CategoriaCargo()
    categoria.nombre = "Docente"
    return categoria
    
def nuevoOrientacion():
    orientacion = Orientacion()
    orientacion.nombre = "Orientacion1"
    return orientacion  