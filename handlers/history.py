import logging
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from database.db import UserCommand

# Настройка логирования
logger = logging.getLogger(__name__)


async def user_history(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_message.chat_id
    user_id = update.effective_user.id

    # Получаем историю команд пользователя из базы данных
    commands = UserCommand.select().where(UserCommand.user_id == user_id).order_by(UserCommand.timestamp.desc()).limit(
        10)

    if commands:
        history_text = "Последние команды:\n"
        for command in commands:
            history_text += f"{command.timestamp}: {command.command}\n"
        await context.bot.send_message(chat_id=chat_id, text=history_text)
    else:
        await context.bot.send_message(chat_id=chat_id, text="История команд не найдена.")


history_handler = CommandHandler('history', user_history)
