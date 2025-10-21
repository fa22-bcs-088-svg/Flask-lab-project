# FROM python:3.10-slim
# WORKDIR /app
# COPY . .
# RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 5000
# CMD ["python", "main/app.py"]
# Use official Nginx image
FROM nginx:alpine

# Remove default nginx web files
RUN rm -rf /usr/share/nginx/html/*

COPY member2_frontend/templates/ /usr/share/nginx/html/
COPY member2_frontend/static/ /usr/share/nginx/html/static/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
