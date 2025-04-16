# Imagen base
FROM python:latest

# Establecer directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código completo
COPY . .

# Variable por defecto de entorno
ENV FLASK_ENV=production

# Puerto que expondrá el contenedor
EXPOSE 5000

