print('Введите предел для совершенных чисел')
lenght = int(input())
k = 0
print("Все совершенные числа до", lenght, ":")
for i in range(1,lenght+1):
    k = 0
    for j in range(1,i):
        if i % j == 0 :
            k += j
    if i == k:
        print(i)

