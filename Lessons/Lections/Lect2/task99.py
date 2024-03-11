
d = {1: 'one', 2: 'two'}
s = d.get(0) or 'Нету'
s1 = d.get(2, 'Нема')
print(s, s1)