# Definir la imagen base sobre la cual se contruirá el contenedor
FROM nginx:alpine

# Copiar los archivos de la aplicación al directorio predeterminado de Nginx
COPY . /usr/share/nginx/html

# Exponer el puerto 80 para el tráfico web
EXPOSE 80