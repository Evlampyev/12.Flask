### POST запрос
>Для отправки POST запроса нашему серверу введём в терминале следующую строку:

curl -X 'POST' 'http://127.0.0.1:8000/items/' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'

>Эта строка отправляет POST запрос на URL-адрес «http://127.0.0.1:8000/items/» с
данными JSON, содержащими поля «имя», «описание», «цена» и «налог» вместе с
соответствующими значениями. Заголовки «accept» и «Content-Type» имеют
значение «application/json», мы пересылаем запросом json объект на сервер и хотим
получить json в качестве ответа.

curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'

### PUT запрос
>Для отправки PUT запроса нашему серверу введём в терминале следующую строку:

curl -X 'PUT' 'http://127.0.0.1:8000/items/42' \
-H 'accept:application/json' \
-H 'Content-Type: application/json' \
-d '{"name": "NewName", "description": "New description of the object", "price": 77.7, "tax": 10.01}'

curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "NewName", "description": "New description of the object", "price": 77.7, "tax": 10.01}'

>Эта строка отправляет HTTP-запрос PUT на локальный сервер по адресу
http://127.0.0.1:8000/, обновляя элемент с идентификатором 42 новой
информацией, предоставленной в формате JSON, такой как имя, описание, цена и налог.
Мы можем опускать необязательные поля объекта Item в запросе. Ответ от сервера
будет 200. А вот отсутствие обязательных параметров приведёт к ответу 422 Unprocessable Entity
