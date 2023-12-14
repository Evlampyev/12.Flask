"""Сессии"""

from flask import Flask, request, make_response, render_template, session, redirect, \
    url_for

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    if 'username' in session: # если есть ключ в сессии
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)  # Удаление значения по ключу username
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
