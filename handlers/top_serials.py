import logging
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from api.kinopoisk import get_top_100_serials
from database.db import UserCommand

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def top_100_serials(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_message.chat_id
    user_id = update.effective_user.id

    # Сохраняем команду в базу данных
    UserCommand.create(user_id=user_id, command='top_100_serials')

    data = get_top_100_serials()
    if data and 'docs' in data:
        serials_list = ""
        for idx, serial in enumerate(data['docs'], start=1):
            name = serial.get('name') or serial.get('alternativeName') or "Не указано"
            year = serial.get('year', "Не указано")
            description = serial.get('shortDescription') if serial.get('shortDescription') else "Описание отсутствует"
            rating = serial.get('rating', {}).get('kp', 'Нет рейтинга')
            serial_info = f"{idx}. {name} ({year}) (Рейтинг: {rating}) - {description}\n"

            # Обход лимита в 4000 сообщений в ТГ
            if len(serials_list) + len(serial_info) > 4000:
                await context.bot.send_message(chat_id=chat_id, text=f"Топ 100 сериалов:\n{serials_list}")
                serials_list = serial_info
            else:
                serials_list += serial_info

        if serials_list:  # Отправка оставшихся сериалов
            await context.bot.send_message(chat_id=chat_id, text=f"Топ 100 сериалов:\n{serials_list}")
    else:
        await context.bot.send_message(chat_id=chat_id, text="Не удалось получить список топ 100 сериалов.")


top_serials_handler = CommandHandler('top_100_serials', top_100_serials)
