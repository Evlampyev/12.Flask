"""
Эта программа создает 5 процессов и запускает функцию increment() в каждом из
них. Функция increment() увеличивает значение глобальной переменной counter на
10 тысяч раз. Весь код работает многопроцессорно, но из-за того, что несколько
процессов работают с одной переменной, может возникнуть проблема гонки
данных (race condition), когда результат выполнения программы может быть
непредсказуемым
"""
import multiprocessing

counter = 0


def increment():
    global counter
    for _ in range(10_000):
        counter += 1
    print(f"Значение счетчика: {counter:_}")


if __name__ == '__main__':
    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=increment)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Значение счетчика: {counter:_}")
