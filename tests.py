# class UserIn():
#     name: int = 5
#     email: int = 7
#
# def create_user(user: UserIn):
#     print(user.dict())
#
#
# us = create_user({'name': 5})

from random import randint, random
import datetime
#
# def generate_rnd_st(n: int = 3):
#     """ Генерация случайной строки из n символов (латиница, нижний регистр)"""
#     return ''.join([chr(randint(97, 122)) for _ in range(n)])
#
#
# print(generate_rnd_st(30))

d0 = '01.01.90'
d1 = '25.03.24'
s0 = datetime.datetime.strptime(d0, '%d.%m.%y').date()
s1 = datetime.datetime.strptime(d1, '%d.%m.%y').date()
dat = (s1 - s0) * random() + s0


