import logging
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from api.kinopoisk import get_top_100_movies
from database.db import UserCommand

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def top_100_movies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_message.chat_id
    user_id = update.effective_user.id

    # Сохраняем команду в базу данных
    UserCommand.create(user_id=user_id, command='top_100_movies')

    data = get_top_100_movies()
    if data and 'docs' in data:
        movies_list = ""
        for idx, movie in enumerate(data['docs'], start=1):
            name = movie.get('name') or movie.get('alternativeName') or "Не указано"
            year = movie.get('year', "Не указано")
            description = movie.get('shortDescription') if movie.get('shortDescription') else "Описание отсутствует"
            rating = movie.get('rating', {}).get('kp', 'Нет рейтинга')
            movie_info = f"{idx}. {name} ({year}) (Рейтинг: {rating}) - {description}\n"

            # Обход лимита в 4000 сообщений в ТГ
            if len(movies_list) + len(movie_info) > 4000:
                await context.bot.send_message(chat_id=chat_id, text=f"Топ 100 фильмов:\n{movies_list}")
                movies_list = movie_info
            else:
                movies_list += movie_info

        if movies_list:  # Отправка оставшихся фильмов
            await context.bot.send_message(chat_id=chat_id, text=f"Топ 100 фильмов:\n{movies_list}")
    else:
        await context.bot.send_message(chat_id=chat_id, text="Не удалось получить список топ 100 фильмов.")


top_movies_handler = CommandHandler('top_100_movies', top_100_movies)
