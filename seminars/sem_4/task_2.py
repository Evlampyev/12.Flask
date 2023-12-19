"""Загрузка сайтов через многопроцесовость"""
# Здесь мы используем модуль multiprocessing для создания процессов вместо
# потоков. Остальной код аналогичен предыдущему примеру.

import requests
from multiprocessing import Process, Pool
import time
from time import time
urls = ['https://github.com/Evlampyev/12.Flask/tree/main',
        'https://ru.wikipedia.org/wiki/Заглавная_страница',
        ]


def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace(
        '/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)


processes = []


if __name__ == '__main__':
    start_time = time()
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Program end at: {time() - start_time :.3f} seconds')