import logging
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from api.kinopoisk import get_random_movie
from database.db import UserCommand

# Настройка логирования
logger = logging.getLogger(__name__)


async def random_movie(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_message.chat_id
    user_id = update.effective_user.id

    # Сохраняем команду в базу данных
    UserCommand.create(user_id=user_id, command='random_movie')

    data = get_random_movie()
    if data:
        movie_info = (
            f"Название: {data.get('name', 'N/A')}\n"
            f"Год: {data.get('year', 'N/A')}\n"
            f"Рейтинг: {data.get('rating', {}).get('kp', 'N/A')}\n"  # Только рейтинг Кинопоиска
            f"Описание: {data.get('description', 'N/A')}"
        )
        await context.bot.send_message(chat_id=chat_id, text=movie_info)
    else:
        await context.bot.send_message(chat_id=chat_id, text="Не удалось получить случайный фильм.")


random_movie_handler = CommandHandler("random_movie", random_movie)
