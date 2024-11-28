from .start import start_handler
from .help import help_handler
from .search import search_movie_handler, message_handler
from .top_movies import top_movies_handler
from .top_serials import top_serials_handler
from .callback_handler import callback_handler
from .random_movie import random_movie_handler
from .history import history_handler
from loader import application

# Добавление обработчиков команд
application.add_handler(start_handler)
application.add_handler(help_handler)
application.add_handler(search_movie_handler)
application.add_handler(message_handler)
application.add_handler(top_movies_handler)
application.add_handler(top_serials_handler)
application.add_handler(callback_handler)
application.add_handler(random_movie_handler)
application.add_handler(history_handler)
