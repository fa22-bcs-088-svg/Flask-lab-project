# Base image
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .
EXPOSE 5000

# Run Flask
CMD ["python", "app.py"]