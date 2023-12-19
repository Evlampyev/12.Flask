# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.

import os
from threading import Thread
from time import time


def count_words(file: str):
    with open(file, 'r', encoding='utf-8') as f:
        words = f.read().split()
        print(f'File {file} contains {len(words)} words')


if __name__ == '__main__':
    start_time = time()
    files = os.listdir('./')
    for file in files:
        thread = Thread(target=count_words, args=[file])
        thread.start()
        thread.join()
    print(f'Program end at: {time() - start_time:.3f} seconds')
