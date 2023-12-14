# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить", при нажатии на которую будет
# произведен подсчет количества слов в тексте и переход на страницу с результатом


from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/result/')
def result():
    text = request.form.get('user_text')
    print(text)
    print(f'{type(text) = }')
    len_text = len(text.split())
    return render_template('result.html', text=text, length=len_text)


if __name__ == '__main__':
    app.run(debug=True)
