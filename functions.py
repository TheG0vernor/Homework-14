from database import base_years, base_genre


def range_of_years(_1, _2):
    """Находит фильмы по диапазону лет"""
    new_list = []
    for i in base_years():
        if int(_2) >= i[1] >= int(_1):
            dict_ = {'title': i[0],
                     'release_year': i[1]}
            new_list.append(dict_)
    return new_list


def search_genre(gen):
    """Находит фильмы по жанру, сортирует по году и выводит 10 результатов"""
    new_list = []  # создадим общий список словарей
    for i in base_genre():
        if gen.upper() in i[2].upper():
            dict_ = {'title': i[0],
                     'release_year': i[1],
                     'description': i[3][:-1]}
            new_list.append(dict_)
    new_list_sorted = sorted(new_list, key=lambda function: function['release_year'], reverse=True)  # отсортируем список словарей по годам выпуска
    new_list_dict = []
    for i in new_list_sorted[:10]:  # обрежем до нужного количества результатов, уберём ключ 'release_year'
        dict_ = {'title': i['title'],
                 'description': i['description']}
        new_list_dict.append(dict_)
    return new_list_dict
