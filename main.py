import logging
from loader import application
from handlers import (
    start_handler,
    help_handler,
    search_movie_handler,
    message_handler,
    top_movies_handler,
    top_serials_handler,
    callback_handler,
    random_movie_handler,
    history_handler
)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the bot")

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(search_movie_handler)
    application.add_handler(message_handler)
    application.add_handler(top_movies_handler)
    application.add_handler(top_serials_handler)
    application.add_handler(callback_handler)
    application.add_handler(random_movie_handler)
    application.add_handler(history_handler)

    application.run_polling()
