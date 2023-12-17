# Создать базу данных для хранения информации о студентах университета. База данных
# должна содержать две таблицы: "Студенты" и "Факультеты". В таблице "Студенты"
# должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов
# с указанием их факультета.

from flask import Flask, request, render_template
from seminars.sem_3.task_1.model_1 import db, Student, Faculty
from string import ascii_lowercase as alphabet
from random import sample, randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem_3_database.db'

db.init_app(app)


@app.route('/')
def index():
    students = Student.query.all()
    context = {'students': students}
    return render_template('index.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('ОК')


@app.cli.command('add-faculty')
def add_faculty():
    facult = ['Математика', "Физика", "Спортсмены"]
    for i in range(len(facult)):
        fact = Faculty(faculty_name=facult[i])
        db.session.add(fact)
    db.session.commit()


@app.cli.command('add-stud')
def add_student():
    """Добавление пользователя в db"""
    genders = [True, False]
    for _ in range(10):
        name = ''.join(sample(alphabet, 4)).title()
        last_name = ''.join(sample(alphabet, 6)).title()
        age = randint(18, 35)
        gender = genders[age % 2]
        group = ''.join(sample(alphabet, 15)).title()
        id_fact = age % 3 + 1
        student = Student(name=name, last_name=last_name, age=age, gender=gender,
                          group=group, faculty_id=id_fact)
        db.session.add(student)
    db.session.commit()
    print('student add')


if __name__ == '__main__':
    app.run(debug=True)
