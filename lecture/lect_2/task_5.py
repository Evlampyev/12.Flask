from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # Представление upload в первую очередь делает проверку на метод запроса
    if request.method == 'POST':
        # Получив post с файлом, сохраняем его в переменной file
        file = request.files.get('file')
        # Чтобы избежать проблем с плохими именами используем
        # функцию secure_filename из модуля werkzeug.utils
        file_name = secure_filename(file.filename)
        # У полученного файла (переменная file) есть метод save. Передав в него путь,
        # происходит действительное сохранение присланного файла
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    # Первоначальный Get запрос приведёт к отрисовки шаблона upload.html
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
