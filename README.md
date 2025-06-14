# Веб-приложение "Интернет-магазин"

## Описание  
Простое веб-приложение, имитирующее интерфейс интернет-магазина. Реализовано с использованием HTML, CSS (Bootstrap) и Python. Содержит четыре страницы:  
- **Главная**
- **Каталог**
- **Категории**
- **Контакты**

Обработка запросов реализована с помощью стандартной библиотеки Python — `http.server`. При переходе на любую страницу открываются соответствующие HTML-шаблоны.

## Цель проекта  
- Освоение верстки с использованием Bootstrap  
- Работа с серверной частью на Python  
- Понимание базовой структуры веб-приложения  
- Обработка GET-запросов

## 📁 Структура проекта

- `web_app/` — директория с исходниками проекта
      - `index.html` — Главная
  - `catalog.html` — Каталог
  - `categories.html` — Категории
  - `contacts.html` — Контакты
- `main.py` — основной серверный скрипт
- `README.md` — описание проекта

## Установка и запуск

1. Клонируйте репозиторий:  
   git clone https://github.com/ваш-ник/ваш-проект.git

2. Перейдите в папку проекта:  
   cd ваш-проект

3. Убедитесь, что у вас установлен Python 3.x. Запустите сервер:  
   python main.py

4. Откройте браузер и перейдите по адресу:  
   http://localhost:8000

## Использование

- Навигация доступна через боковое меню.
- Все страницы отображаются при GET-запросе.
- Страница **Контакты** содержит форму, но сервер её не обрабатывает.

