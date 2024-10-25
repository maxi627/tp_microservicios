# Imagen base de Python
FROM python:3.10-slim-bullseye

# Variables de entorno
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/flaskapp/.local/bin

# Crear usuario y establecer directorio de trabajo
RUN useradd --create-home --home-dir /home/flaskapp flaskapp
WORKDIR /home/flaskapp

# Cambiar a usuario flaskapp y crear directorio app
USER flaskapp
RUN mkdir app

# Copiar el contenido del código de la aplicación y el archivo principal
COPY . .

# # Agregar y instalar las dependencias
# ADD requirements.txt ./requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Flask
EXPOSE 5000

# Comando de ejecución de la aplicación Flask
CMD [ "python", "./stock.py" ]
