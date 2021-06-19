# python con debian como sistema operativo
FROM python:slim


# instalamos nano (editor de texto super ligero)
RUN apt update && apt install nano

# Creamos una carpeta dentro del sistema de linux y la usamos como ruta por defecto, para almacenar nuestra aplicación
WORKDIR /app

# Copiamos todos los archivos desde la carpeta de desarrollo a esa carpeta dentro de la imagen
COPY . /app

# Instalamos las dependecias
RUN pip3 --no-cache install -r ./requirements.txt

# Exponemos el puerto 5000 en el contenedor para que se sepa que vamos a usar ese puerto. (en este caso para pruebas)
EXPOSE 5000

# Lista de ejecuciones
CMD ["python3", "./main.py"]
