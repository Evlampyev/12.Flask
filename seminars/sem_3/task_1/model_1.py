from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(100), nullable=False)
    students = db.relationship('Student', backref='faculty')

    def __repr__(self) -> str:
        return f'Faculty({self.faculty_name})'

    def __str__(self) -> str:
        return self.faculty_name


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    group = db.Column(db.String(50), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Student({self.name}, {self.last_name}, {self.age}, {self.gender}, {self.group})'
