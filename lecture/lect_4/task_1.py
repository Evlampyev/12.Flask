import threading
import time


def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()  # стартуем поток

for t in threads:
    """ t.start()   если стартовать здесь, то будет выполнено один поток, 
                     то есть синхронное выполнение
    """
    t.join()

print("Все потоки завершили работу")

# если t.start() перед t.join() потоки запускаются и
# завершаются последовательно, блокируя выполнение программы на время
# выполнения каждого потока
