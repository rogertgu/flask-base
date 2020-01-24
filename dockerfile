# python con debian como sistema operativo
FROM python:slim


# instalamos nano (editor de texto super ligero)
RUN apt update && apt install nano


# Creamos una carpeta dentro del sistema de linux, para almacenar nuestra aplicación
WORKDIR /app

# Copiamos todos los archivos a esa carpeta
COPY . /app

# Instalamos las dependecias
RUN pip3 --no-cache install -r ./requirements.txt

EXPOSE 5000

# Lista de ejecuciones
CMD ["python3", "./main.py"]
