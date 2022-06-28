import sqlite3, json


def base_film(title):
    """Возвращает фильм по названию"""
    film = sqlite3.connect('netflix.db').cursor().execute(f"""
    SELECT title, country, release_year, listed_in, description
    FROM netflix
    WHERE title LIKE '%{title}%'
    AND title IS NOT NUll
    ORDER BY release_year DESC
    """).fetchone()
    sqlite3.connect('netflix.db').close()

    dict_ = {  # создадим словарь фильму
                "title": film[0],
                "country": film[1],
                "release_year": film[2],
                "genre": film[3],
                "description": film[4][:-1]
            }
    return dict_


def base_years():
    """Возвращает список фильмов с лимитом для дальнейшего поиска по диапазону лет"""
    base_years_ = sqlite3.connect('netflix.db').cursor().execute("""
    SELECT title, release_year
    FROM netflix
    LIMIT 100
    """).fetchall()
    sqlite3.connect('netflix.db').close()
    return base_years_


def base_rating():
    """Возвращает список фильмов для дальнейшего поиска по рейтингу"""
    films_rat = sqlite3.connect('netflix.db').cursor().execute("""
    SELECT title, rating, description
    FROM netflix
    WHERE rating != ''
    LIMIT 100
    """).fetchall()
    sqlite3.connect('netflix.db').close()
    return films_rat


def base_genre():
    """Возвращает список фильмов для дальнейшего поиска по жанру"""
    films_genre = sqlite3.connect('netflix.db').cursor().execute("""
    SELECT title, release_year, listed_in, description
    FROM netflix
    LIMIT 100
    """).fetchall()
    sqlite3.connect('netflix.db').close()
    return films_genre


def base_names_actors(_1, _2):
    """Возвращает актёров, которые участвовали в съёмках более 2 раз вместе с указанными актёрами"""
    with sqlite3.connect('netflix.db') as base_actors:
        cursor = base_actors.cursor()
        execute_ = cursor.execute(f"""
        SELECT netflix.cast
        FROM netflix
        WHERE netflix.cast != ''
        AND netflix.cast LIKE '%{_1}%'
        AND netflix.cast LIKE '%{_2}%'
        """).fetchall()

    list_ = []
    for i in execute_:
        list_2 = '.'.join(list(i))  # переведём список кортежей в один большой список
        list_.extend(list_2.split(', '))

    if _1 in list_:
        list_.remove(_1)
    if _2 in list_:
        list_.remove(_2)  # удалим значения, которые не нужны

    list_set = []
    for i in range(len(list_)):
        if list_.count(list_[i]) > 2:  # определим, каких актёров больше 2
            list_set.append(list_[i])

    list_set = set(list_set); list_set = tuple(list_set)  # удалим повторяющиеся значения; возведём в список (кортеж)
    return list_set


def base_search_movies(type_, year, genre):
    """Возвращает фильмы, которые соответствуют типу, году и жанру"""
    with sqlite3.connect('netflix.db') as base_actors:
        execute_ = base_actors.cursor().execute(
            f"""
        SELECT title, description
        FROM netflix
        WHERE type LIKE '%{type_}%'
        AND release_year = {year}
        AND listed_in LIKE '%{genre}%'
        """).fetchall()

    list_all = []
    for i in execute_:  # создадим список словарей из списка кортежей
        dict_ = {
         "title": i[0],
         "description": i[1][:-1]
            }
        list_all.append(dict_)
    return json.dumps(list_all)
