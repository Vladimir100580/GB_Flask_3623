import threading

n = 10 # Количество потоков
counter = [0] * n
print(counter)

def increment(m):
    global counter
    for _ in range(5_000_000):
        counter[m] += 1
    print(f"Значения счетчиков: {counter = }")


threads = []
for i in range(n):
    t = threading.Thread(target=increment, args=(i, ))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"Значения счетчиков в финале: {counter = }")
