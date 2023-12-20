from aiohttp import ClientSession
import asyncio
from time import time

urls = ['https://github.com/Evlampyev/12.Flask/tree/main',
        'https://ru.wikipedia.org/wiki/Заглавная_страница',
        ]


async def download_content(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace(
                '/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_content(url))
        # создаем асинхронную задачу для каждого сайта из списка urls
        tasks.append(task)
        # добавляем задачу в список tasks
        await asyncio.gather(*tasks)  # выполни асинхронно все tasks


if __name__ == '__main__':
    start_time = time()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    print(f'Program end at: {time() - start_time:.3f} seconds')
