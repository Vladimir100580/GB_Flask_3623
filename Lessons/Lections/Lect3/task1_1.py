import time


def fibonacci(m):
    """ Нахождение n-го числа ряда Фибоначчи"""
    if m in (1, 2):
        return 1
    return fibonacci(m - 1) + fibonacci(m - 2)

x = []
y = []
for n in range(1, 43):
    beg = time.time()
    fb = fibonacci(n)
    time_r = time.time() - beg
    x.append(n)
    y.append(time_r)
    print(f'{n = }, {fb = }, {time_r = }')

print(*x, sep='\n')
print(*[str(i).replace('.', ',') for i in y], sep='\n')
