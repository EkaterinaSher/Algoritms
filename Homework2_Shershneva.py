#Задание 1

def recur():

    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = input('Введите знак: ')

    if c != '0':
        if c == '+':
            print(a+b)
            recur()
        elif c == '-':
            print(a-b)
            recur()
        elif c == '*':
            print(a*b)
            recur()
        elif c == '/' and b != 0:
            print(a/b)
            recur()
        elif c == '/' and b == 0:
            print('На 0 делить нельзя')
            recur()
        elif c != '+' or c != '-' or c != '/' or c != '*' or c != 0:
            print('Ведите верный знак операции')
            recur()
    else:
        print('Выход из программы')
        return 0 


recur()

#Задание 2

odd = 0
even = 0

def rec2(numbs):
    global odd
    global even

    if len(numbs) > 1:
        if int(numbs[-1:]) % 2 == 0:
            even += 1
            rec2(numbs[:-1])
        else:
            odd += 1
            rec2(numbs[:-1])

    else:
        if int(numbs) % 2 == 0:
            even += 1
        else:
            odd += 1
        print("odd = " + str(odd) + " even = " + str(even))

y = input("Введите число: ")
rec2(y)

#Задание 3

f = ""

def rec3(numerus):
    global f

    if len(numerus) > 1:
        f = f + numerus[-1:]
        rec3(numerus[:-1])
    else:
        f = f + numerus
        print(f)



a = input("Введите число: ")
rec3(a)

#Задание 4

elem = 1
x = 1

def sum_el (n):
    global elem
    global x
    if int(n) > 1:
        x = ((x)*(-1))/2
        elem = elem + x
        sum_el (int(n)-1)

    else:
        print("Сумма элементов = " + str(elem))
    


n = input ("Введите количество элементов: ")
sum_el(n)

#Задание 6
import random
item = random.randint(0, 100)
low = 0
high = 100
n = 10

def randm(n):
    x = int(input("Попробуйте угадать число: "))
    print("left" + str(n))

    if n > 0:
        if x > item:
            print("Меньше, попробуйте еще раз")
            randm(n-1)

        elif x < item:
            print("Больше, попробуйте еще раз")
            randm(n-1)

        elif x == item:
            print("Вы угадали!")

    else:
        print("Ваши попытки закончились, это число = " + str(item))

randm(n)


