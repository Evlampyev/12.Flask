# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year_of_publishing = db.Column(db.Integer, nullable=False)
    number_of_copies = db.Column(db.Integer, nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self) -> str:
        return f'Books({self.name}, {self.year_of_publishing})'

    def __str__(self):
        return f'{self.name} {self.year_of_publishing}'


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    books = db.relationship('Books', backref='authors')

    def __repr__(self) -> str:
        return f'Authors({self.name}, {self.last_name})'

    def __str__(self):
        return f'{self.name} {self.last_name}'
