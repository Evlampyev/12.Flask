# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте потоки.

import threading
import requests
from time import time

urls = ['https://github.com/Evlampyev/12.Flask/tree/main',
        'https://ru.wikipedia.org/wiki/Заглавная_страница',
        ]


def download_content(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/',
                                                                                    '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)


threads = []
start_time = time()
for url in urls:
    thread = threading.Thread(target=download_content, args=[url])
    # цель для потока - функция download, с аргументом url
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Program end at: {time() - start_time:.3f} seconds')