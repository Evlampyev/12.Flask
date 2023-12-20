# * Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# * Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# * Массив должен быть заполнен случайными целыми числами от 1 до 100.
# * При решении задачи нужно использовать
# * В каждом решении нужно вывести время выполнения вычислений.

from random import randint
import time
from threading import Thread

N = 14
number_of_threads = 4
result = 0


def sum_numbers(array):
    global result
    summa = 0
    for i in array:
        summa += i
    result += summa


if __name__ == '__main__':
    arrs = [randint(1, 10) for _ in range(N)]
    print(arrs)

    arr = []
    step = N // number_of_threads + 1
    for i in range(number_of_threads):
        arr.append(arrs[i * step:(i + 1) * step])
    print(arr)

    threads = []
    start = time.time()

    for ar in arr:
        thread = Thread(target=sum_numbers, args=[ar])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Result: {result}')
    print(f'Program end at: {time.time() - start} seconds')
