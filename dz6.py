# Показать на экран все простые числа в диапазоне,
# указанном пользователем. Число называется простым,
# если оно делится без остатка только на себя и на единицу.
# Например, три — это простое число, а четыре нет.

start = int(input("Начало диапозона: ")) 
end = int(input("Конец: ")) 
 
print("Простые числа") 
for x in range(start, end + 1): 
    if x > 1: 
        for i in range(2, x): 
            if(x % i) == 0: 
                break 
        else: 
            print(x)
# Задание 2
# Показать на экране таблицу умножения для всех чисел
# от 1 до 10. Например:
# 1 * 1 = 1 1 * 2 = 2 ….. 1 * 10 = 10
# .........................................................................
# 10 * 1 = 10 10 * 2 = 20 …. 10 * 10 = 100.

for i in range(1,11):
    for x in range(1,11):
        print(i,"*",x, "=", i*x,end='  ')
    print()


# Задание 3
# Показать на экран таблицу умножения в диапазоне,
# указанном пользователем. Например, если пользователь
# указал 3 и 5, таблица может выглядеть так
# 3*1 = 3 3*2 = 6 3*3 = 9 ... 3 * 10 = 30
# .....................................................................................
# 5*1 = 5 5 *2 = 10 5 *3 = 15 ... 5 * 10 = 50

start_1 = int(input("Начало диапозона: ")) 
end_1 = int(input("Конец: ")) 
for j in range(start_1,end_1+1):
    for p in range(1,11+1):
        print(j,"*",p , "=", j*p,";",end='  ')    
    print()

        

