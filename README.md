![Header](assets/img/ryder_isologotipos.png)

# Pesticidas introducidos silenciosamente (PIS)

Web y switch apps para proyecto "Pesticidas introducidos silenciosamente" (PIS) de Democracia en Red

## Contenido y Fundamentación técnica

Esta web contiene la presentación y explicación del proyecto, como así tambien un mapeo y rutas de las diferentes aplicaciones desarrolladas en otras tecnologías especialmente diseñadas para el procesamiento de datos.

Respecto a la disyuntiva de la elección de la tecnología de front-end ideal para este caso se decidió ir por una tecnología hibrida que pueda hacer de nexo entre los oficios de desarrollo frontend y desarrollo de ciencia de datos.

- [Flask](https://flask.palletsprojects.com/en/2.3.x/), al ser un pequeño framework desarrollado en python, es ideal para acercar los conceptos de html, css y js a cientistas de datos y para acercar terminología y sintaxis de python a desarrolladores front-end.

## Setup

Hay 2 maneras de preparar el entorno para desarrollo. A través de un entorno virtual de python, o a través de Docker

### 1 - Entorno virtual de python (virtualenv)

> #### ⚠️ Prerequisitos
> 
> Este entorno virtual requiere de:
> - [Python 3](https://www.python.org/)
> - [pip](https://www.pypi.org/)
> - [virtualenv](https://pypi.org/project/virtualenv/)

#### Instalación

Abrí una terminal del sistema en el directorio raiz del proyecto, creá el entorno virtual, activalo, instalá las dependencias del proyecto y ejecutá la plataforma

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python main.py
```

#### Ejecución

Abrí una terminal del sistema en el directorio raiz del proyecto, activá el entorno virtual y ejecutá la plataforma


```bash
$ source env/bin/activate
$ python main.py
```

### 2 - Docker

> #### ⚠️ Prerequisitos
> 
> Este entorno virtual requiere de:
> - [Docker](https://docs.docker.com/engine/install/_) y (docker) compose (que en las nuevas versiones ya viene en la instalación de docker)

#### Instalación

Abrí una terminal del sistema en el directorio raiz del proyecto y construí la imagen de docker

```bash
$ docker compose build
```

#### Ejecución

Abrí una terminal del sistema en el directorio raiz del proyecto y ejecutá la imagen en un contenedor

```bash
$ docker compose up
```

## Licencia

El siguiente repositorio es un desarrollo de codigo abierto bajo la licencia GNU General Public License v3.0. Pueden acceder a la haciendo [click aqui](./LICENSE).

