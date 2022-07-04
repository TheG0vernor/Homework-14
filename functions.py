from database import base_years, base_genre, base_rating


def range_of_years(_1, _2):
    """Находит фильмы по диапазону лет"""
    new_list = []
    for i in base_years():
        if int(_2) >= i[1] >= int(_1):
            dict_ = {'title': i[0],
                     'release_year': i[1]}
            new_list.append(dict_)
    return new_list


# def rating_children():
#     """Находит фильмы для детей"""
#     list_children = ('G', 'TV-G', 'TV-Y', 'TV-Y7', 'TV-Y7-FV')
#     new_list = []
#     for i in base_rating():
#         if i[1] in list_children:
#             dict_ = {'title': i[0],
#                      'rating': i[1],
#                      'description': i[2][:-1]}
#             new_list.append(dict_)
#     return new_list
#
#
# def rating_family():
#     """Находит фильмы для семьи"""
#     list_family = ('G', 'PG-13', 'PG', 'TV-PG', 'TV-14', 'TV-Y', 'TV-Y7', 'TV-Y7-FV')
#     new_list = []
#     for i in base_rating():
#         if i[1] in list_family:
#             dict_ = {'title': i[0],
#                      'rating': i[1],
#                      'description': i[2][:-1]}
#             new_list.append(dict_)
#     return new_list
#
#
# def rating_adult():
#     """Находит фильмы для взрослой аудитории"""
#     list_adult = ('NC-17', 'R', 'TV-MA', 'NR', 'UR')
#     new_list = []
#     for i in base_rating():
#         if i[1] in list_adult:
#             dict_ = {'title': i[0],
#                      'rating': i[1],
#                      'description': i[2][:-1]}
#             new_list.append(dict_)
#     return new_list


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
