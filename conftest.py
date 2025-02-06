import pytest
from main import BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def books():
    books = BooksCollector()
    books.books_genre = {
        'Игра Эндера': 'Фантастика',
        'Интерстеллар': 'Фантастика',
        'Кто похитил мой мозг?': 'Детективы',
        'Смешарики': 'Мультфильмы',
        'Веселые истории': 'Комедии'}
    return books

@pytest.fixture
def favorite_books():
    favorite_books = BooksCollector()
    favorite_books.books_genre = {
        'Игра Эндера': 'Фантастика',
        'Интерстеллар': 'Фантастика',
        'Кто похитил мой мозг?': 'Детективы',
        'Смешарики': 'Мультфильмы',
        'Веселые истории': 'Комедии'}
    favorite_books.favorites = [
        'Смешарики',
        'Веселые истории'
    ]
    return favorite_books
