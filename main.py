# numbers = [5, 10, 15, 25]
# print(numbers[::-2])
#
# st = "[2, 4, 6, 9]"
#
# ll = [[3, 2, 'a', 4], [6, 9], [6, 5, 6]]
#
# for i in tuple(enumerate(ll)):
#     print([i[0]] + i[1])
#
# print([[i[0]] + list(i[1]) for i in tuple(enumerate(ll, 1))])
#
#
# lst = [[1, 4], [2, 6], [1, 8]]
# lst.sort(key=lambda a: (a[0], -a[1]))
# print(lst)
from random import randint

for i in range(10):
    count = randint(3, 6)
    a = randint(3, 8)
    while count == a:
        a = randint(3, 8)
    print(f'Палку длиной {a * (count)} разрезали на {count} равны{["e", "х"][count > 4.5]} част{["и", "ей"][count > 4.5]}. '
          f'Найдите длину каждой части.')





