from flask import Flask, request, make_response, render_template

app = Flask(__name__)


# @app.route('/')
# def index():
#     # устанавливаем cookie
#     response = make_response("Cookie установлен")
#     response.set_cookie('username', 'admin')
#     return response

#  модифицируем представление
@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'name' : 'Харитон'
    }
    response = make_response(render_template('main.html', **context))
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', context['name'])
    return response
# Используя render_template пробрасываем контекст в шаблон, но не возвращаем его,
# а передаём результат в функцию make_response. Ответ сформирован, но мы можем
# внести в него изменения перед возвратом. В нашем примере добавили в заголовки
# пару ключ-значение и установили куки для имени пользователя.

@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"


if __name__ == '__main__':
    app.run(debug=True)
