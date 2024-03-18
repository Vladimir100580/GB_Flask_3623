import multiprocessing

n = 10 # Количество потоков
counter = [0] * n
print(counter)

def increment(m):
    global counter
    for _ in range(5_000_000):
        counter[m] += 1
    print(f"Значения счетчиков: {counter = }")


if __name__ == '__main__':
    processes = []
    for i in range(n):
        t = multiprocessing.Process(target=increment, args=(i, ))
        processes.append(t)
        t.start()
    for t in processes:
        t.join()
    print(f"Значения счетчиков в финале: {counter = }")  # Все в 0. Здесь были запущены n отдельных процессов
