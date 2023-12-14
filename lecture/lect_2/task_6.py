import logging
from flask import Flask, render_template, request, abort
from my_func import get_blog  # Функция, которая из БД получает статью по её id

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    ...
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)
    ...
    # возвращаем найденную в БД статью


@app.errorhandler(404)  # декоратора обрабатывает ошибку 404
def page_not_found(e):
    """Вызывается при ошибке 404"""
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url'  : request.base_url,
    }
    return render_template('404.html', **context), 404
    # стандартный код 200 будет заменен на 404


@app.errorhandler(500)  # декоратор обрабатывает 500 ошибку: Ошибку сервера.
def page_not_found(e):
    logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url'  : request.base_url,
    }
    return render_template('500.html', **context), 500


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False) В режиме не разработчика появляется окно при ошибках для пользователя
