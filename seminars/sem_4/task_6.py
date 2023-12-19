# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход.
import asyncio  # асинхронный модуль для работы с событиями
import os
import aiofiles  # асинхронный модуль для работы с файлами
from time import time


async def count_words(file: str):
    words = 0
    async with aiofiles.open(file, mode='r', encoding='utf-8') as f:
        for line in await f.readlines():
            words += len(line.strip().split())  # считаем количество слов в файле

        print(f'File {file} contains {words} words')


async def main():
    files = os.listdir('./')
    tasks = []
    for file in files:
        task = asyncio.ensure_future(count_words(file))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time()
    loop = asyncio.new_event_loop()  # асинхронный цикл событий
    loop.run_until_complete(main())  # запускаем цикл событий до конца работы программы
    print(f'Program end at: {time() - start_time:.3f} seconds')
