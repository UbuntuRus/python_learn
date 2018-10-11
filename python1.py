print('Введите предел для чисел Фибоначчи')
lenght = int(input())
fib = [1, 1]
while fib[-1] < lenght:
    fib.append(fib[-1] + fib[-2])
if fib[-1] > lenght:
    fib.pop()
print('Числа Фибоначчи до заданного предела:', fib)
