# Utiliza una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo en la raíz del proyecto
WORKDIR /app

# Copia los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -U pip wheel
RUN pip install --no-cache-dir -r requirements.txt

