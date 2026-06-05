# 🏋️ Zadanie 9 - System Organizacji Treningów Fitness

Projekt zaliczeniowy realizujący system zarządzania aktywnościami fizycznymi, wykonany zgodnie z architekturą MVC w technologii Django na ocenę celującą.

## 📋 Spis treści
1. Funkcjonalności
2. Struktura bazy danych (Modele)
3. Instrukcja uruchomienia (Klasyczna)
4. Instrukcja uruchomienia (Docker)

## ✨ Funkcjonalności (Wymagania na wyższą ocenę)
- **Pełny CRUD**: Możliwość dodawania, przeglądania, edycji oraz usuwania treningów bezpośrednio z poziomu interfejsu użytkownika.
- **Relacyjne Modele (ForeignKey)**: Wydzielenie osobnego modelu dla kategorii treningowych (`Category`) i powiązanie go relacją klucza obcego z głównym modelem treningu (`Workout`).
- **Dynamiczny interfejs (Dropdown)**: Formularz dodawania i edycji automatycznie renderuje listę opcji kategorii pobieraną dynamicznie bezpośrednio z bazy danych.
- **Zaawansowana Wyszukiwarka**: Filtrowanie danych w bazie po nazwie treningu lub powiązanej kategorii przy użyciu obiektów `Q`.
- **Walidacja danych**: Weryfikacja poprawności wprowadzanej intensywności w skali 1-10 po stronie klienta (HTML5) oraz serwera (Django Validators).
- **Estetyczny frontend**: Widok oparty na komponentach Bootstrap 5 z nowoczesnymi, dynamicznymi paskami postępu odzwierciedlającymi poziom intensywności treningu.
- **Konteneryzacja (Docker)**: Środowisko zostało w pełni przygotowane do uruchomienia wewnątrz niezależnych kontenerów.

## 🗄️ Struktura projektowa MVC
- **Model (M)**: 
  - `Category` (pole: `nazwa`)
  - `Workout` (pola: `nazwa`, `category` [ForeignKey], `intensywnosc`)
- **Kontroler (V - views.py)**: Obsługa żądań HTTP (GET/POST), filtrowanie za pomocą QuerySetów, interakcja z modelami oraz przekazywanie danych do szablonów.
- **Widok (T - templates)**: Pliki `list.html` (główny dashboard), `form.html` (wspólny formularz do tworzenia i edycji) oraz `confirm_delete.html` (potwierdzenie usunięcia).

## 🚀 Instrukcja obsługi (Klasyczna)
1. Sklonuj repozytorium i przejdź do folderu projektu.
2. Stwórz i aktywuj środowisko wirtualne:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Na systemach macOS/Linux

   pip install -r requirements.txt

   python manage.py runserver

## Uruchomienie za pomocą dockera:
docker-compose up --build