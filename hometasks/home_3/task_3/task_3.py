# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и
# оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок

from hometasks.home_3.task_3.model_3 import db, Students, Scores, Items
from flask import render_template, request, redirect, url_for, flash, Flask
from random import randint, choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_3_task_3_db.db'

db.init_app(app)


@app.route('/')
def index():
    students = Students.query.all()
    context = {}
    stud = {}
    for student in students:
        st_id = student.name + ' ' + student.last_name
        print(st_id)
        stud[st_id] = Scores.query.filter(Scores.id_student == student.id).all()
        print(stud[st_id])
    context['students'] = stud
    return render_template('index.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('add-items')
def add_items():
    db.session.add(Items(name='Высшая математика'))
    db.session.add(Items(name='История России'))
    db.session.add(Items(name='Педагогика'))
    db.session.add(Items(name='Информатика'))
    db.session.commit()
    print("Items added")


@app.cli.command('add-students')
def add_students():
    for i in range(10):
        name = f'Student_' + str(i)
        last_name = f'Last_name_' + str(i)
        group = f'Another group_' + str(i % 3)
        gender = choice(['мужчина', 'женщина'])
        email = name + '@mail.ru'
        student = Students(name=name, last_name=last_name, group=group, gender=gender,
                           email=email)
        db.session.add(student)
    db.session.commit()
    print('student added')


@app.cli.command('add-score')
def add_score():
    for i in range(20):
        students_number = len(Students.query.all())
        items_number = len(Items.query.all())
        score = randint(2, 5)
        id_student = randint(0, students_number)
        item_name = randint(0, items_number)
        new_mark = Scores(score=score, id_student=id_student, item_name=item_name)
        db.session.add(new_mark)
    db.session.commit()
    print("Score added")
