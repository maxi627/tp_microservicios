# Imagen base de Python
FROM python:3.10-slim-bullseye

# Instalar dependencias necesarias para mysqlclient y psycopg2
RUN apt-get update && \
    apt-get install -y \
    default-libmysqlclient-dev \  
    pkg-config \                 
    libpq-dev \                 
    build-essential \          
    && rm -rf /var/lib/apt/lists/* 

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

# Copiar solo el archivo de requisitos primero para aprovechar la caché
COPY requirements.txt ./requirements.txt

# Agregar y actualizar pip y setuptools antes de instalar dependencias
RUN pip install --upgrade pip setuptools

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido del código de la aplicación y el archivo principal
COPY . .

# Exponer el puerto de Flask
EXPOSE 5000

# Comando de ejecución de la aplicación Flask
CMD ["python", "./stock.py"]
