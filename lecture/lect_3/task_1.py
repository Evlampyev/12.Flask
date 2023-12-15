from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# для подключения к БД sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# для подключения к mysql+pymysql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/database_name'
# для подключения к postgresql+psycopg2
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://username:password@hostname/database_name'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    app.run(debug=True)
