import logging
from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes
from handlers.top_movies import top_100_movies
from handlers.top_serials import top_100_serials
from handlers.search import search_movie
from handlers.random_movie import random_movie
from handlers.history import user_history
from handlers.start import start_menu

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'top_100_movies':
        await top_100_movies(update, context)
        await start_menu(update, context)
    elif query.data == 'top_100_serials':
        await top_100_serials(update, context)
        await start_menu(update, context)
    elif query.data == 'search_movie':
        await search_movie(update, context)
        # Не вызываем start_menu здесь, так как будем вызывать его после получения результатов поиска
    elif query.data == 'random_movie':
        await random_movie(update, context)
        await start_menu(update, context)
    elif query.data == 'history':
        await user_history(update, context)
        await start_menu(update, context)


callback_handler = CallbackQueryHandler(button_handler)
