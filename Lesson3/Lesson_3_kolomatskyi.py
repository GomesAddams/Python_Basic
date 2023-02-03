#TASK_1

import random

print(dir(random))

min = (random.randint(0, 59))

print(min)


if (0 <= min and min <= 15) :

    print("Число знаходиться у першій чверті")

elif (16 <= min and min <= 30) :

    print("Число знаходиться у другій чверті")

elif (31 <= min and min <= 45) :

    print("Число знаходиться у третій чверті")

elif (46 <= min and min <= 59) :

    print("Число знаходиться у четвертій чверті")

#TASK_2

print("Введіть номер місяця вашого народження: ")

birth_month = int(input())


if birth_month == 1 or birth_month == 2 or birth_month == 12:

    print("Зима - За вікном падав сніг.")

elif birth_month == 3 or birth_month == 4 or birth_month == 5:

    print("Весна - Все довкола розцвітало.")

elif birth_month == 6 or birth_month == 7 or birth_month == 8:

    print("Літо - Діти насолоджувались літніми канікулами.")

elif birth_month == 9 or birth_month == 10 or birth_month == 11:

    print("Осінь - Все довкола загоралось яскравими фарбами.")

elif birth_month > 12:

    print("Введіть номер місяця від 1 до 12.")

#TASK_3

a = (random.randint(0, 999999))

print(a)

#if (a // 6) is int:

if ((a(-1)) % 2 == 0) and sum == 0:



    while (a != 0):
        sum = sum + a % 10

        a = a // 10

    print("Сумма усіх цифр дорівнює: ", sum)

    if (sum // 3) is int:

        print("Число sum ділиться на 3.")

    else:

        print("Число sum не ділиться на 3.")

    print("Число a ділиться на 6.")

else:

    print("Число a не ділиться на 6.")




#TASK_4

print("Введіть координати X : ")

x = float(input())

print("Введіть координати Y : ")

y = float(input())

if (x > 0 and y > 0):

    print("Точка розташована у першій чверті")

elif (x < 0 and y > 0):

    print("Точка розташована у другій чверті")

elif (x < 0 and y < 0):

    print("Точка розташована у третій чверті")

elif (x > 0 and y < 0):

    print("Точка розташована у четвертій чверті")

elif (x == 0 and y == 0):

    print("Точка розташована на початку координат")