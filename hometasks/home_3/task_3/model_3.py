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

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    group = db.Column(db.String(100), nullable=False, default='Информатики')
    gender = db.Column(db.Enum('мужчина', 'женщина'), nullable=False, default='мужчина')
    email = db.Column(db.String(100), nullable=False, default='')

    def __repr__(self):
        return f'Student({self.id}, {self.name}, {self.last_name})'

    def __str__(self):
        return '<Student %r>' % self.name


class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    id_student = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    item_name = db.Column(db.Integer, db.ForeignKey('items.name'), nullable=False)

    def __str__(self):
        return f'{self.item_name} {self.id_student} {self.score}'


class Items(db.Model):
    name = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)

    def __str__(self):
        return self.name
