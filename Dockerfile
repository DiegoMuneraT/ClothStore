# Utiliza una imagen base con Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el código de tu proyecto al contenedor
COPY . .

# Cambia al directorio de la aplicacion
WORKDIR /app/clothstore

# Expone el puerto en el que se ejecutará la aplicación de Django (ajusta el puerto según tus necesidades)
EXPOSE 8000

# Comando para ejecutar la aplicación de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]