SISTEMA BASE
==================


### Descripción

Este proyecto pretende servir de base para otros proyectos, ya incluyendo algunas características comunes para todos los proyectos que tengan una api y un administrador con django jet con Django 5

## Requermientos

1. Python 3.11
2. pip 23.2.1

## Instalación

1. Creación de un entorno virtual: `mkvirtualenv -p python3.11 base` o `mkvirtualenv base` si solo esta instalado python 3.11 
2. Instalar pip version 23 `pip install pip==23.2.1`
2. Instalacion de dependencias: `pip install -r requirements/development.txt`
3. Creacion de una base de datos. (Preferentemente PostgreSQL)
4. Configuracion del proyecto desde el archivo `.env`: `cp env.example .env`
5. Correr migraciones. `python manage.py migrate`
6. Si se quiere importar provincias/departamentos/localidades: `python manage.py importar_ubicaciones`
