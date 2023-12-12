from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'name' : "Alex",
        'title': 'All is main',
    }
    return render_template('index_2.html', **context)


@app.route('/poems/')
def poems():
    context = {
        'poem': ['Вот не думал, не гадал,',
                 'Программистом взял и стал.',
                 'Хитрый знает он язык,',
                 'Он к другому не привык.',
                 ]
    }
    # txt = """<h1>Стихотворение</h1>\n<p>""" +'<br/>'.join(poem) + '</p>'
    return render_template('poems.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
