from app.models import * 
#-----------------------------------------------------------------------------
# DEPARTAMENTO
#-----------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------
# ORIENTACION
#-----------------------------------------------------------------------------
def nuevoOrientacion():
    orientacion = Orientacion()
    orientacion.nombre = "Orientacion1"
    return orientacion 
   
def nuevoOrientacion2():
    orientacion = Orientacion()
    orientacion.nombre = "Orientacion2"
    return orientacion

#-----------------------------------------------------------------------------
# MATERIA
#-----------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------
# AUTORIDAD
#-----------------------------------------------------------------------------
def nuevaAutoridad():
    autoridad = Autoridad()
    autoridad.nombre = "Juan Perez"
    autoridad.telefono = "123456789"
    autoridad.email = "email123@mail.com"
    autoridad.cargo = nuevoCargo()
    return autoridad

#-----------------------------------------------------------------------------
# CARGO
#-----------------------------------------------------------------------------
def nuevoCargo():
    cargo = Cargo()
    cargo.nombre = "Profesor"
    cargo.puntos = 10
    cargo.categoria_cargo = categoriaCargo()
    cargo.tipo_dedicacion = tipoDeCargo()
    return cargo

def nuevoCargo2():
    cargo = Cargo()
    cargo.nombre = "Decano"
    cargo.puntos = 100
    cargo.categoria_cargo = categoriaCargo2()
    cargo.tipo_dedicacion = tipoDeCargo2()
    return cargo

def nuevoCargo3():
    cargo = Cargo()
    cargo.nombre = "Vicedecano"
    cargo.puntos = 80
    cargo.categoria_cargo = categoriaCargo3()
    cargo.tipo_dedicacion = tipoDeCargo3()
    return cargo

#-----------------------------------------------------------------------------
# CATEGORIA CARGO
#-----------------------------------------------------------------------------
def categoriaCargo():
    categoria = CategoriaCargo()
    categoria.nombre = "Docente"
    return categoria

def categoriaCargo2():
    categoria_cargo = CategoriaCargo()
    categoria_cargo.nombre = "Categoria 1"
    return categoria_cargo

def categoriaCargo3():
    categoria_cargo = CategoriaCargo()
    categoria_cargo.nombre = "Categoria 2"
    return categoria_cargo

#-----------------------------------------------------------------------------
# TIPO DEDICACION
#-----------------------------------------------------------------------------
def tipoDeCargo():
    tipo = TipoDedicacion()
    tipo.nombre = "Tiempo completo"
    return tipo

def tipoDeCargo2():
    tipo_dedicacion = TipoDedicacion()
    tipo_dedicacion.nombre = "Simple"
    tipo_dedicacion.observacion = "Observacion 1"
    return tipo_dedicacion

def tipoDeCargo3():
    tipo_dedicacion = TipoDedicacion()
    tipo_dedicacion.nombre = "Simple2"
    tipo_dedicacion.observacion = "Observacion 2"
    return tipo_dedicacion



#-----------------------------------------------------------------------------
# ESPECIALIDAD
#-----------------------------------------------------------------------------
def nuevaEspecialidad():
    especialidad = Especialidad()
    especialidad.nombre = "Especialidad 1"
    especialidad.letra = "a"
    especialidad.observacion = "Observacion 1"
    return especialidad

def nuevaEspecialidad2():
    especialidad = Especialidad()
    especialidad.nombre = "Especialidad 2"
    especialidad.letra = "b"
    especialidad.observacion = "Observacion 2"
    return especialidad
