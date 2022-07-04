from flask import Flask, request, jsonify
from functions import range_of_years, search_genre
from database import base_film, base_rating


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False


@app.route('/movies/<title>', methods=['GET'])  # поиск фильма
def search_movie(title):
    return jsonify(base_film(title))


@app.route('/movie/')  # поиск фильмов по диапазону
def year_to_year():
    from_ = request.args.get('from')
    to = request.args.get('to')
    return jsonify(range_of_years(from_, to))


@app.route('/rating/<rating>')  # фильмы в зависимости от рейтинга
def films_for_children(rating):
    return jsonify(base_rating(rating))


# @app.route('/rating/children/')  # фильмы для детей
# def films_for_children():
#     return jsonify(rating_children())
#
#
# @app.route('/rating/family/')  # фильмы для семьи
# def films_for_family():
#     return jsonify(rating_family())
#
#
# @app.route('/rating/adult/')  # фильмы для взрослых людей
# def films_for_adult():
#     return jsonify(rating_adult())


@app.route('/genre/<genre>', methods=['GET'])  # поиск фильмов по жанру
def films_by_genre(genre):
    return jsonify(search_genre(genre))


if __name__ == '__main__':
    app.run()
