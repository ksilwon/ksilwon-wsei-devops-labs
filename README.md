# Projekt DevOps - WSEI 🚀

Projekt zaliczeniowy realizujący automatyzację procesów CI/CD dla aplikacji webowej.

## 📋 Spis treści
- [O aplikacji](#-o-aplikacji)
- [Uruchomienie lokalne](#-uruchomienie-lokalne)
- [Konteneryzacja (Docker)](#-konteneryzacja-docker)
- [Pipeline CI/CD](#-pipeline-cicd)
- [Zarządzanie projektem](#-zarządzanie-projektem)

---

## 💻 O aplikacji
Aplikacja została napisana w technologii **Python (FastAPI)**. Udostępnia dwa wymagane punkty końcowe (endpoints):
* `GET /`: Zwraca komunikat powitalny JSON.
* `GET /products`: Zwraca przykładową listę produktów w formacie JSON.

Aplikacja posiada zestaw testów jednostkowych (`pytest`), które weryfikują poprawność działania powyższych ścieżek.

---

## 🛠 Uruchomienie lokalne

### Wymagania
* Python 3.12+
* pip

### Instalacja i start
1. Zainstaluj zależności:
   pip install -r requirements.txt
   
2. Uruchom serwer deweloperski:
   uvicorn main:app --reload

3. Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000

---

## 🐳 Konteneryzacja (Docker)
Projekt zawiera `Dockerfile`, co pozwala na uruchomienie aplikacji w odizolowanym środowisku.

1. Zbuduj obraz:
   docker build -t devops-wsei-app .
   
2. Uruchom kontener:
   docker run -p 80:80 devops-wsei-app

---

## 🏗 Pipeline CI/CD
Automatyzacja została oparta o **GitHub Actions**:

1. **Continuous Integration (CI)**:
   * Uruchamia się przy każdym `Pull Request` do gałęzi `main`.
   * Instaluje zależności, buduje projekt i wykonuje testy jednostkowe.

2. **Continuous Delivery (CD)**:
   * Uruchamia się automatycznie po mergu do gałęzi `main`.
   * Wdraża aplikację na platformę **Azure App Service**.

---

## 📊 Zarządzanie projektem
Postępy prac są monitorowane przy użyciu **GitHub Projects** (tablica Kanban).

---

