Тесты
Добавление книг
	•	test_add_new_book_valid_name_success: Проверяет успешное добавление книги с корректным названием в коллекцию.
	•	test_add_new_book_duplicate_name_should_not_add: Убеждается, что дублирующиеся названия книг не добавляются в коллекцию.
	•	test_add_new_book_not_valid_name_should_not_add: Проверяет, что книги с некорректными или пустыми названиями не добавляются.
	•	test_add_new_book_valid_name_add_with_empty_genre: Убеждается, что новая книга добавляется с пустым жанром по умолчанию.
Управление жанрами
	•	test_set_book_genre_existing_genre_success: Проверяет успешное присвоение жанра существующей книге.
	•	test_get_book_genre_existing_name_sucess: Убеждается, что метод возвращает правильный жанр для существующей книги.
	•	test_get_book_genre_non_existing_book_return_none: Проверяет, что метод возвращает None для несуществующей книги.
Получение книг по жанру
	•	test_get_books_with_specific_genre_existing_genre_return_books: Проверяет, что метод возвращает список книг для существующего жанра.
	•	test_get_books_with_specific_genre_no_books_return_empty_list: Убеждается, что метод возвращает пустой список для несуществующего жанра.
Работа с избранными книгами
	•	test_add_book_in_favorite_name_add_in_favorite: Проверяет добавление книги в список избранных.
	•	test_delete_book_from_favorite_name_delete_from_list: Убеждается, что книга удаляется из списка избранных.
	•	test_get_list_of_favorites_books_sucess: Проверяет, что метод возвращает корректный список избранных книг.
Работа со списком детский книг
	•	test_get_books_for_children_return_books: Проверяет, что метод возвращает список книг, подходящих для детей.
