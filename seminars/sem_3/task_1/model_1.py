from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_ket=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    group = db.Column(db.String(50), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeygnKey('faculty'))

    def __repr__(self):
        return Student(f'{self.first_name} {self.second_name}')


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_ket=True)
    faculty_name = db.Column(db.String(50), nullable=False)
    students = db.relationship('Student', backref='', lazy=True)

    def __repr__(self):
        return Faculty(f'{self.id} {self.faculty_name}')