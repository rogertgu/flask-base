# Plantilla de Proyecto Web Básico con Python y Docker

Este repositorio contiene una plantilla para iniciar rápidamente un proyecto web básico utilizando Python, Flask, Bulma CSS y Docker. Esta plantilla es ideal para desarrolladores que deseen crear aplicaciones web simples en Python y desplegarlas utilizando contenedores Docker.

## Características

- Estructura básica de proyecto Flask.
- Plantillas Jinja2 con un diseño básico utilizando Bulma CSS.
- Archivos de configuración para Docker y Docker Compose.
- Archivo .env para la gestión de variables de entorno.
- Archivos .gitignore y .dockerignore para un mejor control de versiones.

## Requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/) (opcional, solo si deseas ejecutar el proyecto fuera de Docker)

## Uso

1. Clona este repositorio en tu máquina local:
    
    ```bash
    git clone https://github.com/rogertgu/flask-base
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd flask-base
    ```

3. Edita el archivo .env según tus necesidades (app name, author etc.)
    ```bash
    nano .env
    ```

4. Construye la imagen de Docker:

    ```bash
    docker-compose build
    ```

5. Lanza el contenedor de Docker:

    ```bash
    docker-compose up -d
    ```

6. Accede a la aplicación web en tu navegador:

    ```bash
    http://localhost:5000
    ```

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## personalización

- Cambiar el nombre del proyecto y el autor en el archivo .env
- Cambiar el nombre del proyecto en el archivo docker-compose.yml
- Edita el archivo main.py y agrega tus propias rutas y controladores según las necesidades de tu aplicación.
- Actualiza los archivos de plantilla en la carpeta templates con el contenido y diseño de tu aplicación.
- Añade tus propios archivos JavaScript en la carpeta static/js y enlázalos en las plantillas según sea necesario.
- Si necesitas instalar dependencias adicionales, añádelas al archivo requirements.txt.
