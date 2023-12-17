from seminars.sem_3.task_2.model_2 import db
from flask import Flask, render_template, request
from random import randint, sample, choice
from seminars.sem_3.task_2.model_2 import Books, Authors

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem_3_task_2_db.db'

db.init_app(app)


@app.route('/')
def index():
    books = Books.query.order_by(Books.year_of_publishing)
    return render_template('index.html', books=books)


@app.cli.command('db-init')
def db_init():
    db.create_all()
    print('OK')


@app.cli.command('add-authors')
def add_authors():
    for i in range(3):
        name = 'Author_' + str(i)
        last_name = 'Last_name_' + str(i)
        author = Authors(name=name, last_name=last_name)
        db.session.add(author)
    db.session.commit()
    print('author added')


@app.cli.command('add-books')
def add_books():
    for i in range(10):
        name = f'Book_' + str(i)
        year_of_publishing = randint(1900, 2020)
        number_of_copies = randint(1, 10)
        author = Authors.query.order_by(db.func.random()).first()
        book = Books(name=name, year_of_publishing=year_of_publishing,
                     number_of_copies=number_of_copies, id_author=author.id)
        db.session.add(book)
    db.session.commit()
    print('book added')