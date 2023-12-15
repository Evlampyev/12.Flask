# Создать базу данных для хранения информации о студентах университета. База данных
# должна содержать две таблицы: "Студенты" и "Факультеты". В таблице "Студенты"
# должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов
# с указанием их факультета.

from flask import Flask
from model_1 import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://mydatabase.db'

db.init_app(app)


@app.route('/')
def index():
    students = Student.query.all()
    return


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('ОК')


if __name__ == '__main__':
    app.run(debug=True)
