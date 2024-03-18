import threading
import time
from random import randint

def worker(num):
    print(f"Начало работы потока {num}")
    o = randint(1, 15)
    print(o)
    time.sleep(o)
    print(f"\nКонец работы потока {num}")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, ))
    threads.append(t)
    print(f'{threads = }')
    t.start()
for t in threads:
    # t.start() так будет последовательно
    t.join()
print("Все потоки завершили работу")
