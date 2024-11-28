# Telegram Movie Bot 🎬

## 📖 Описание проекта

**Telegram Movie Bot** — это телеграм-бот, который использует API КиноПоиска для предоставления информации о фильмах и сериалах. Бот позволяет искать фильмы, получать топовые рейтинги, случайные рекомендации и многое другое. 

---

## 🚀 Основной функционал

- **Поиск фильмов**: находите информацию о фильмах по названию.
- **Топовые рейтинги**: отображение топ-100 фильмов и сериалов.
- **Случайные фильмы**: рекомендации фильмов с высоким рейтингом.
- **История запросов**: сохранение и просмотр истории команд.

---

## 🛠 Используемые технологии

- **Python**
- **Telegram Bot API** с библиотекой `python-telegram-bot`
- **КиноПоиск API** для получения информации о фильмах
- **SQLite** для хранения истории запросов
- **dotenv** для работы с конфиденциальными данными

---

## 📋 Команды бота

| Команда              | Описание                             |
|----------------------|-------------------------------------|
| `/start`             | Начало работы с ботом              |
| `/help`              | Список доступных команд            |
| `/top_100_movies`    | Топ-100 фильмов                    |
| `/top_100_serials`   | Топ-100 сериалов                   |
| `/search <название>` | Поиск фильма по названию           |
| `/random_movie`      | Случайный фильм с рейтингом 7+     |
| `/history`           | История выполненных запросов       |

---

## ⚙️ Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/DanilaZhuravlev/telegram_movie_bot.git

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
3. Получите API КиноПоиска (при необходимости):
   [kinopoisk.dev](https://kinopoisk.dev/)

5. Создайте файл .env в корневой директории и добавьте ключи API:
   ```bash
   TELEGRAM_TOKEN=ваш_токен_телеграм
   KINOPOISK_API_TOKEN=ваш_токен_кинопоиска

6. Запустите бота:
   ```bash
   python main.py
  
---

## 🛡 Заметки по безопасности

- Храните **.env** файл в недоступном для других месте.
- Не выкладывайте **токены API** в **публичные репозитории.**


## 📷 Примеры использования

**Топ 100**  
  ![image](https://github.com/user-attachments/assets/f42de094-be05-497e-bdc8-56db661bf2b4)

 **Поиск фильма**  
![Screenshot_6](https://github.com/user-attachments/assets/5f7d46d5-45a4-41af-a63b-0c35e9e9ac2b)




---

---

## 📬 Контакты
Автор: Данила Журавлев

GitHub: [DanilaZhuravlev](https://github.com/DanilaZhuravlev)
