

FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install flask

# Expose port 80 (optional, good practice)
EXPOSE 80

# Run Flask on port 80 and 0.0.0.0
CMD ["python", "-u", "app.py"]
