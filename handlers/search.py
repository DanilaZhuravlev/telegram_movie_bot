import logging
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext
from api.kinopoisk import get_movie_data
from handlers.start import start_menu
from database.db import UserCommand

# Настройка логирования
logger = logging.getLogger(__name__)

# Глобальный словарь для хранения состояния поиска пользователя
user_search_state = {}


async def search_movie(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id if update.message else update.callback_query.message.chat_id
    user_id = update.message.from_user.id if update.message else update.callback_query.from_user.id

    # Сохраняем команду в базу данных
    UserCommand.create(user_id=user_id, command='search')

    # Запрашиваем название фильма
    await context.bot.send_message(chat_id=chat_id, text="Введите название фильма:")

    # Устанавливаем состояние ожидания названия фильма для пользователя
    user_search_state[chat_id] = 'awaiting_movie_name'


# Функция для обработки текстового сообщения от пользователя
async def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    user_state = user_search_state.get(chat_id)

    if user_state == 'awaiting_movie_name':
        movie_name = update.message.text
        logger.info(f"Searching for movie: {movie_name}")
        data = get_movie_data(movie_name)

        if data:
            logger.info(f"Received data: {data}")
            if 'docs' in data and len(data['docs']) > 0:
                first_movie = data['docs'][0]
                movie_info = (
                    f"Название: {first_movie.get('name', 'N/A')}\n"
                    f"Год: {first_movie.get('year', 'N/A')}\n"
                    f"Рейтинг: {first_movie.get('rating', {}).get('kp', 'N/A')}\n"  # Только рейтинг Кинопоиска
                    f"Описание: {first_movie.get('description', 'N/A')}"
                )
                await update.message.reply_text(movie_info)
            else:
                await update.message.reply_text("Фильм не найден.")
        else:
            logger.error("No data received from API")
            await update.message.reply_text("Фильм не найден.")

        # Сбрасываем состояние пользователя после поиска
        user_search_state.pop(chat_id, None)

        # Возвращаем стартовое меню
        await start_menu(update, context)


search_movie_handler = CommandHandler("search", search_movie)
message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
