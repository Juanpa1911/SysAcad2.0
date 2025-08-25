# SYSACAD 2.0 - Desarrollo de Software
## Integrantes
- López Laszuk Juan Pablo
- Piastrellini Mariano
- Buttini Cristobal
- Sosa Ricardo
- Iriarte López Ana Valentina
- Moya Carlos
- Github Copilot

SYSACAD 2.0 es un sistema académico desarrollado en Python. Diseñado bajo una arquitectura en capas, con un enfoque de desarrollo guiado por pruebas (TDD).

> ⚡ La arquitectura de SYSACAD 2.0 está estructurada en múltiples capas y módulos especializados, garantizando la separación de responsabilidades:
models - repositories - services - mapping - resources - tests

---
## Requerimientos (hasta ahora)
- Docker Dekstop
- PlantUML
- POSTMAN
- PostgreSQL 14.17-bookworm
- Python 3.15.5
- Flask==3.1.0
- Flask-SQLAlchemy==3.1.1
- SQLAlchemy==2.0.40
- psycopg2==2.9.10
- psycopg[binary]
- python-dotenv==1.1.0
- Flask-Migrate==4.1.0
- flask-marshmallow==1.3.0
- marshmallow==4.0.0
- weasyprint==65.1
- python-odt-template==0.5.1
- docxtpl==0.20.0
- markupsafe== 3.0.2

---

## 📂 Descripcion Modulos Principales del proyecto 

```
SYSACAD 2.0/
├── models/             # Definiciones de tablas como objetos usando a SQLALCHEMY (ORM)
├── repositories/       # Acceso y persistencia en BD (SQLAlchemy)
├── services/           # Lógica de negocio 
├── test/               # Pruebas unitarias (verifican solo la conexion con service)
├── mapping/            # Serialización, deserialización y validación de datos
├── resources/          # Recursos REST que exponen la API (Solicitudes HTTP)
├── db/                 # Configuración de sesión SQLAlchemy
├── config/             # Lectura de variables de entorno (.env)
├── .env                # Variables de entorno. Contiene la URI de conexión a PostgreSQL
├── requirements.txt    # Dependencias necesarias
└── README.md           # Documentacion principal 
```

## Guia para la ejecucion de los TEST
Para testear las clases es necesario contar con una base de datos en la cual se pueda realizar los testeos.
Se va a utilizar PostgreSQL para la base de datos y se creará un contenedor en Docker Desktop.

---
## Paso 1
En el repositorio se debe crear un archivo `.env` y debe escribir lo siguiente:
```env
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_RECORD_QUERIES = True
TEST_DATABASE_URI='postgresql+psycopg2://usuario:contraseña@localhost:5433/TEST_SYSACAD'
DEV_DATABASE_URI='postgresql+psycopg2://usuario:contraseña@localhost:5433/DEV_SYSACAD'
PROD_DATABASE_URI='postgresql://usuario:contraseña@localhost:5433/SYSACAD'
```
Luego se debe cambiar usuario, contraseña y puerto según los valores que correspondan.
### Explicación del codigo de arriba:
El fragmento de código está relacionado con la configuración de una aplicación en Flask que utiliza SQLAlchemy como ORM (Object Relational Mapper).
🔧 Parámetros de configuración
- SQLALCHEMY_TRACK_MODIFICATIONS = False
Desactiva el sistema de seguimiento de modificaciones de objetos.

Esto mejora el rendimiento y evita una advertencia (warning) innecesaria.

✅ Recomendado dejar en False si no vas a usar señales del modelo.

- SQLALCHEMY_RECORD_QUERIES = True
Activa el registro de las consultas SQL ejecutadas.

Útil para depuración, análisis de rendimiento y profiling.

Normalmente se utiliza en entornos de desarrollo o testing.
URIs de conexión a bases de datos
Cada URI define cómo conectarse a una base de datos PostgreSQL distinta, y están pensadas para distintos entornos:

- TEST_DATABASE_URI
Conecta a la base de datos de pruebas llamada TEST_SYSACAD en:
```makefile
host: localhost
puerto: 5433
usuario: usuario
contraseña: contraseña
```
- DEV_DATABASE_URI
Conecta la base de datos de desarrollo DEV_SYSACAD en el mismo host y puerto.

- PROD_DATABASE_URI
Conecta la base de datos de producción SYSACAD.
Usa el mismo host y puerto, aunque no tiene especificado +psycopg2, lo que puede implicar que use el controlador por defecto de SQLAlchemy para PostgreSQL (aunque no es obligatorio si psycopg2 es el único instalado).

**En resumen**
Esto configura los parámetros de SQLAlchemy y define cómo conectarse a tres bases de datos diferentes para:
- Testing
- Desarrollo
- Producción
---
## Paso 2
En una carpeta aparte del repositorio crear una carpeta llamada docker y clonar este repositorio: 
https://github.com/umpprats/microservicios.git, van a borrar todas las carpetas menos la de PostgreSQL

![image](https://github.com/user-attachments/assets/14144578-f6d4-4eee-9b11-51a3f873146e)

El archivo ``.env`` debe renombrarse borrando el "**-example**", luego debe abrirse y cambiar los valores del archivo por su usuario, contraseña y nombre de la base de datos
```env
POSTGRES_PASSWORD=CONTRASEÑA
POSTGRES_DB=NOMBRE DE LA BASE DE DATOS
POSTGRES_USER=USUARIO
```
Ahora para configurar el archivo `docker-compose.yml` debe abrirse con Visual Studio.
```YAML
services:    
  postgresql:
    container_name: postgresql-servidor  # Nombre del contenedor en Docker
    image: postgres:15.4-bullseye        # Imagen de PostgreSQL que se descarga
    ports:
      - "5432:5432"                      # Mapea el puerto 5432 del host al contenedor
    networks:
      - mired                            # Nombre de la red Docker (debe coincidir con la red externa)
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}  # Variables de entorno (no modificar, se toman del entorno)
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - ./data:/var/lib/postgresql/data           # Persistencia de datos
      - ./sql:/docker-entrypoint-initdb.d         # Scripts SQL de inicialización
    restart: always                                # Reiniciar automáticamente si se cae

networks:
  mired:           # Reemplazar 'mired' por el nombre real de tu red Docker
    external: true # Indica que la red ya existe y es externa
```

---
## Paso 3
En docker, abrir la terminal, moverse dentro de la carpeta PostgreSQL (clonada en el paso anterior) y ejecutar dentro de ella los siguiente comandos:

```bash
# Ir a la carpeta del repositorio
cd "ruta/del/repositorio"

# Crear la red Docker (el nombre debe coincidir con el usado en docker-compose.yml)
docker network create nombre_de_la_red

# Levantar los contenedores definidos en docker-compose.yml
docker compose up
```
Esto empezará a crear la base de datos, toma unos segundos. Una vez terminada la creación de la base de datos, aparecerán 3 opciones. Debe presionarse la letra **v**, esta llevará a Docker. Ubicarse en conteiners para visualizar el conteiner creado.

---

## Paso 4
Abrir el repositorio en el IDE con el que se trabaja, en nuestro caso Visual Studio Code, es necesario tener instalada la extensión `Database Client JDBC` para poder conectarse a la base de datos.

Una vez que el cliente fue instalado, debe abrirse desde la barra de tareas y precionar click en crear una nueva base de datos.

![image](https://github.com/user-attachments/assets/595d150a-8a53-407a-ad2c-b873d1811625)

Colocar la configuración de la base de datos (Es importante que el contenedor este encendido desde el DOCKER, si no, no funcionara)

![image](https://github.com/user-attachments/assets/3c383a25-6b0d-4923-a7cd-64fdcfa32944)

Se habrá creado la lista, presionar `+` y colocar las líneas que se verán a continuación. Se ejecutan para crear las 2 bases de datos que se configuraron al principio:
```SQL
CREATE DATABASE "TEST_SYSACAD"
CREATE DATABASE "DEV_SYSACAD"
```

Ahora la base de datos esta lista para realizar los testeos de las clases!

![image](https://github.com/user-attachments/assets/182c766c-366b-4777-b88f-0746058085ec)

---

## Pasos para la ejecución de la aplicacion
Para garantizar una correcta inicialización del proyecto, se recomienda seguir el siguiente procedimiento.

En una nueva terminal ejecutar los siguiente comandos:

1. **Crear el entorno virtual en la carpeta raiz del proyecto**  
   ➜ `python -m venv venv`

2. **Activar el entorno virtual (necesario para instalar las librerias de requirements.txt )**  
   ➜ `.\venv\Scripts\Activate.ps1`

3. **Instalar las librerías y dependencias especificadas en requirements.txt**  
   ➜ `pip install -r requirements.txt`

  Una vez instaladas correctamente todas las librerias y dependencias especificadas en el archivo requirements.txt se puede proceder con la ejecucion de la aplicacion
  
4. **Ejecucion de la Aplicacion**
   ➜ `python app.py `
   

