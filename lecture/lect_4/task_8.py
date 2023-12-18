import asyncio
from pathlib import Path


async def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        # do some processing with the file contents
        print(f'{f.name} содержит <<<{contents[:7]}...>>>')


async def main():
    # dir_path = Path('/path/to/directory')
    dir_path = Path('.') # получаем путь к текущей директории
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    # перебираем все объекты в директории, если это файл, то добавляем его в file_paths
    tasks = [asyncio.create_task(process_file(file_path)) for file_path in file_paths]
    # с каждым файлом создается корутина process_file
    await asyncio.gather(*tasks)
    # запускаются все задачи, которые выполняются паралельно


if __name__ == '__main__':
    asyncio.run(main())
