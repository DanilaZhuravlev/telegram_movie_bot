import logging
from telegram.ext import ApplicationBuilder
from config.config import TELEGRAM_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
