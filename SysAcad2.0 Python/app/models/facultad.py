from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Facultad:
    nombre : str
    abreviatura : str
    directorio : str
    sigla : str
    codigo_postal : str
    ciudad : str
    domicilio : str
    telefono : str
    contacto :  str 
    email : str
    