import requests
from config.config import KINOPOISK_API_TOKEN
import logging

# URL API для поиска фильмов
api_url = 'https://api.kinopoisk.dev/v1.4/movie/search'
movie_url = 'https://api.kinopoisk.dev/v1.4/movie'
random_movie_url = 'https://api.kinopoisk.dev/v1.4/movie/random'

# Настройка логирования
logger = logging.getLogger(__name__)


def get_movie_data(movie_name):
    headers = {
        'accept': 'application/json',
        'X-API-KEY': KINOPOISK_API_TOKEN
    }
    params = {
        'page': 1,
        'limit': 10,
        'query': movie_name,
        'notNullFields': ["name", "alternativeName"],
        'selectFields': ["name", "alternativeName", "year", "shortDescription", "rating",]
    }
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        response_data = response.json()
        logger.debug(f"API response data: {response_data}")
        return response_data
    else:
        logger.error(f"Error: Received status code {response.status_code}")
        logger.error(f"Response: {response.text}")
        return None


def get_top_100_movies():
    headers = {
        "accept": "application/json",
        "X-API-KEY": KINOPOISK_API_TOKEN
    }
    params = {
        "page": 1,
        "limit": 100,
        "lists": "top250",
        "notNullFields": ["name", "alternativeName"],
        "sortField": ["rating.kp"],
        "sortType": ["-1"],
        "selectFields": ["name", "alternativeName", "year", "shortDescription", "rating"]
    }
    response = requests.get(movie_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Error: Received status code {response.status_code}")
        logger.error(f"Response: {response.text}")
        return None


def get_top_100_serials():
    headers = {
        "accept": "application/json",
        "X-API-KEY": KINOPOISK_API_TOKEN
    }
    params = {
        "page": 1,
        "limit": 100,
        "lists": "series-top250",
        "type": "tv-series",
        "typeNumber": ["2"],
        "notNullFields": ["name", "alternativeName"],
        "sortField": ["rating.kp"],
        "sortType": ["-1"],
        "selectFields": ["name", "alternativeName", "year", "shortDescription", "rating"]
    }
    response = requests.get(movie_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Error: Received status code {response.status_code}")
        logger.error(f"Response: {response.text}")
        return None


def get_random_movie():
    headers = {
        'accept': 'application/json',
        'X-API-KEY': KINOPOISK_API_TOKEN
    }
    params = {
        'notNullFields': ["name", "shortDescription", "rating.kp", "genres.name"],
        'rating.kp': '7-10'
    }
    response = requests.get(random_movie_url, headers=headers, params=params)
    if response.status_code == 200:
        response_data = response.json()
        logger.debug(f"API response data: {response_data}")
        return response_data
    else:
        logger.error(f"Error: Received status code {response.status_code}")
        logger.error(f"Response: {response.text}")
        return None
