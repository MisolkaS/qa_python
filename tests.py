import pytest

class TestBooksCollector:
    @pytest.mark.parametrize('name',
                             ['Три мушкетера',
                              '1']
                             )
    def test_add_new_book_valid_name_success(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.books_genre

    def test_add_new_book_duplicate_name_should_not_add(self, collector):
        collector.add_new_book('Дубли книги')
        collector.add_new_book('Дубли книги')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('name',
                             ['',
                              'Имя книги очень-очень преочень длинное, длиннее сорока одного символа']
                             )
    def test_add_new_book_not_valid_name_should_not_add(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_valid_name_add_with_empty_genre(self, collector):
        name = 'Три Мушкетера'
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''

    def test_set_book_genre_existing_genre_success(self, collector):
        name = 'Игра Эндера2'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.books_genre[name] == 'Фантастика'

    def test_get_book_genre_existing_name_sucess(self, books):
        assert books.get_book_genre('Игра Эндера') == 'Фантастика'

    def test_get_books_genre(self, books):
        all_books = {
            'Игра Эндера': 'Фантастика',
            'Интерстеллар': 'Фантастика',
            'Кто похитил мой мозг?': 'Детективы',
            'Смешарики': 'Мультфильмы',
            'Веселые истории': 'Комедии'
        }
        assert books.get_books_genre() == all_books

    def test_get_book_genre_non_existing_book_return_none(self, books):
        assert books.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre_existing_genre_return_books(self, books):
        fantasy_books = books.get_books_with_specific_genre('Фантастика')
        expected_books = ['Игра Эндера', 'Интерстеллар']
        assert all(book in fantasy_books for book in expected_books)

    def test_get_books_with_specific_genre_no_books_return_empty_list(self, books):
        assert books.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_for_children_return_books(self, books):
        children_books = books.get_books_for_children()
        expected_books = ['Игра Эндера', 'Смешарики', 'Веселые истории', 'Интерстеллар']
        assert all(book in children_books for book in expected_books)

    def test_add_book_in_favorite_name_add_in_favorite(self, books):
        name = 'Смешарики'
        books.add_book_in_favorites(name)
        assert name in books.books_genre

    def test_delete_book_from_favorite_name_delete_from_list(self, favorite_books):
        name = 'Смешарики'
        favorite_books.delete_book_from_favorites(name)
        assert name not in favorite_books.favorites

    def test_get_list_of_favorites_books_sucess(self, favorite_books):
        favorites = favorite_books.get_list_of_favorites_books()
        expected_books = ['Смешарики', 'Веселые истории']
        assert all(book in favorites for book in expected_books)