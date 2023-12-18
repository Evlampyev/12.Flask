"""Загрузка сайтов через асинхронную функцию"""
# Здесь мы используем модуль asyncio для асинхронной загрузки страниц. Мы
# создаем функцию download, которая использует aiohttp для получения
# html-страницы и сохранения ее в файл. Затем мы создаем асинхронную функцию
# main, которая запускает функцию download для каждого сайта из списка urls и
# ожидает их завершения с помощью метода gather. Мы запускаем функцию main с
# помощью цикла событий asyncio

import asyncio
import aiohttp  # асинхронный модуль для получения html-страниц, аналог requests
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace(
                '/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        # создаем асинхронную задачу для каждого сайта из списка urls
        tasks.append(task)
        # добавляем задачу в список tasks
        await asyncio.gather(
            *tasks)  # выполни асинхронно все tasks


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
