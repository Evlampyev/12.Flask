"""Чтобы работал файл запускать через wsgi.py в корне  с ссылкой на app этого файла"""
from datetime import datetime, timedelta

from flask import Flask, render_template, jsonify
# render_template - отрисовывает шаблоны через jinja
from lecture.lect_3.task_2.model_02 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data'


@app.route('/users/')
def all_users():
    """Вывод всех пользователей"""
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_username(username):
    """Вывод только пользователей username"""
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content,
              'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})


#     jsonify - возвращает информацию не в виде html, а в виде json файла

@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content,
              'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})


@app.cli.command("init-db")
def init_db():
    """Покажет ошибку с неверным wsgi.py"""
    db.create_all()
    print('OK')


@app.cli.command("add-john")
def add_user():
    """Добавление пользователя в db"""
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


@app.cli.command("edit-john")
def edit_user():
    """Изменение записей в db"""
    user = User.query.filter_by(username='john').first()
    # query - объект запрос
    # filter_by - ключ для фильтрации
    # first - найти первое вхождение
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail in DB!')


@app.cli.command("del-john")
def del_user():
    """Удаление пользователя из db"""
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)  # обращаемся к db -> сессии и удаляем (пользователя)
    db.session.commit()
    print('Delete John from DB!')


@app.cli.command("fill-db")
def fill_tables():
    """Дадфылобавление нескольких пользователей в db"""
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()

    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()
    print('Table "User" and "Post" create')


if __name__ == '__main__':
    app.run(debug=True)
