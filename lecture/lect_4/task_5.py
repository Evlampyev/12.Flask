"""
Чтобы избежать этой проблемы в task_4.py, используется объект multiprocessing.Value, который
обеспечивает безопасный доступ к общей переменной через механизм блокировки
(lock). Каждый процесс получает доступ к переменной только после получения
блокировки, что гарантирует правильность ее изменения
"""
import multiprocessing

counter = multiprocessing.Value('i', 0)


def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock():
            cnt.value += 1
    print(f"Значение счетчика: {cnt.value:_}")


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(counter,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Значение счетчика в финале: {counter.value:_}")
