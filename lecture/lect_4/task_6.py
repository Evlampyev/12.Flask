"""
Эта программа демонстрирует асинхронный код с использованием библиотеки
asyncio. В функциях print_numbers() и print_letters() с помощью ключевого слова
await осуществляется ожидание выполнения операции asyncio.sleep(), что
позволяет переключаться между задачами без блокировки выполнения программы.
В функции main() создаются две задачи, которые выполняются параллельно, а
затем ожидается их завершение
"""
import asyncio


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        print(letter)
        await asyncio.sleep(0.5)  # передача ресурсов другим корутинам


async def main():
    task1 = asyncio.create_task(print_numbers())  # задача №1
    task2 = asyncio.create_task(print_letters())  # задача №1
    await task1
    await task2


asyncio.run(main())
