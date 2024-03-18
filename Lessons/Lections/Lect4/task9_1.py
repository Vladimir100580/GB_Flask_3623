import multiprocessing

n = 8  # количество процессов   (сколько используется в первой строке, столько и ядер у компьютера)
counter = [multiprocessing.Value('i', 0) for _ in range(n)]


def increment(cnt, m):
    for _ in range(50_000):
        with cnt[m].get_lock():   # БЛОКИРОВКА переменной на время прибавления единицы (здесь можно без этого)
            cnt[m].value += 1
    print(f"Значения счетчиков: {[cnt[k].value for k in range(n)]}")


if __name__ == '__main__':
    processes = []
    for i in range(n):
        p = multiprocessing.Process(target=increment, args=(counter, i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print(f"Значения счетчиков в финале: {counter = }")
