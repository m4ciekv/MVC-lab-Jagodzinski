# lekki obraz Pythona
FROM python:3.11-slim

# zmienne środowiskowe, aby Python nie tworzył plików .pyc i nie buforował wyjścia
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# katalog roboczy wewnątrz kontenera
WORKDIR /app

# plik z wymaganiami i instalacja zależności
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie zawartości projektu do katalogu /app
COPY . /app/

# Otwarcie portu 8000, na którym domyślnie działa Django
EXPOSE 8000

# Komenda uruchamiająca serwer po starcie kontenera
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]