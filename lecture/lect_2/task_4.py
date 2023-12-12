from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/submit', methods=['GET', 'POST'])  # view готова обрабатывать оба метода
def submit():
    if request.method == 'POST':  # ветка для метода POST
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')  # ветка для метода GET


#  Ниже две функции представления, у которых явно указаны другие декораторы,
#  указывающие на метод
@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)
