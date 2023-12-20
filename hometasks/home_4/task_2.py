# * Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# * Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# * Массив должен быть заполнен случайными целыми числами от 1 до 100.
# * При решении задачи нужно использовать многопроцессорность.
# * В каждом решении нужно вывести время выполнения вычислений.

import time
from random import randint
from multiprocessing import Process, Manager

N = 10
number_of_process = 4



def sum_numbers(array: list[int], result: dict, key: int) -> None:
    summa = 0
    for num in array:
        summa += num
    print(f"{summa =}")
    result[key] = summa


if __name__ == '__main__':
    arrs = [randint(1, 10) for _ in range(N)]
    print(arrs)

    arr = []
    step = N // number_of_process + 1
    for i in range(number_of_process):
        arr.append(arrs[i * step:(i + 1) * step])
    print(arr)
    manager = Manager()
    result = manager.dict()

    processes = []
    start = time.time()
    for i, ar in enumerate(arr):
        process = Process(target=sum_numbers, args=(ar, result, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Словарь сумм: {result}')
    print(f"Результат: {sum(result.values())}")
    print(f'Program end at: {time.time() - start} seconds')
