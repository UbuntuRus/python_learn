print('Введите предел для простых чисел')
lenght = int(input())
simple = []
n = 2
if lenght >= 2:
    simple.append(2)
if lenght >= 3:
    simple.append(3)
if lenght >= 5:
    simple.append(5)
if lenght >= 7:
    simple.append(7)
#ненужный костыль, наверное
while n < lenght:
     if n%2 != 0 and n%3 != 0 and n%5 != 0 and n%7 != 0:
         simple.append(n)
         n += 1
     else:
         n += 1
print('Все простые числа до заданного предела:', simple)
