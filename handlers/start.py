from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes


async def start_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id if update.message else update.callback_query.message.chat_id

    keyboard = [
        [InlineKeyboardButton("Топ 100 фильмов", callback_data='top_100_movies')],
        [InlineKeyboardButton("Топ 100 сериалов", callback_data='top_100_serials')],
        [InlineKeyboardButton("Поиск фильма", callback_data='search_movie')],
        [InlineKeyboardButton("Рандомный тайтл с рейтингом от 7", callback_data='random_movie')],
        [InlineKeyboardButton("История команд", callback_data='history')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=chat_id, text="Выберите действие:", reply_markup=reply_markup)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_menu(update, context)


start_handler = CommandHandler('start', start)
