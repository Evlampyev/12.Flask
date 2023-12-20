# Задание №7
# * Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# * Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# * Массив должен быть заполнен случайными целыми числами от 1 до 100.
# * При решении задачи нужно использовать асинхронность.
# * В каждом решении нужно вывести время выполнения вычислений.

from time import time
from random import randint
from asyncio import new_event_loop, ensure_future, gather

N = 10
number_of_process = 4
result = 0


async def sum_numbers(array: list[int]):
    summa = 0
    global result
    for num in array:
        summa += num
    print(f"{summa = }")
    result += summa


async def main():
    arrs = [randint(1, 10) for _ in range(N)]
    print(arrs)

    arr = []
    step = N // number_of_process + 1
    for i in range(number_of_process):
        arr.append(arrs[i * step:(i + 1) * step])
    print(arr)
    tasks = []
    for i, ar in enumerate(arr):
        task = ensure_future(sum_numbers(ar))
        tasks.append(task)
        await gather(*tasks)  # выполни асинхронно все tasks


if __name__ == '__main__':
    start_time = time()
    loop = new_event_loop()
    loop.run_until_complete(main())
    print(f'{result = }')
    print(f'Program end at: {time() - start_time:.3f} seconds')
