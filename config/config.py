import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
KINOPOISK_API_TOKEN = os.getenv('KINOPOISK_API_TOKEN')
