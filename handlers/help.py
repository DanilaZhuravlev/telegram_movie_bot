import logging
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Доступные команды\n"
        "/top_100_movies - Показать топ 100 фильмов\n"
        "/top_100_serials - Показать топ 100 сериалов\n"
        "/search - Поиск фильма по названию\n"
        "/random_movie - Рандомный тайтл с рейтингом от 7\n"
    )
    await update.message.reply_text(help_text)


help_handler = CommandHandler('help', help_command)
