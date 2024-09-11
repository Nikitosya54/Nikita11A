#решение задач
#1. меньше из двух
a = int(input("введите первое число: "))
b = int(input("введите вторе число: "))
if a<b:
    print(f"{a} меньшее число")
elif b<a :
    print(f"{b} меньшее число")
else:
    print("числа одинаковые")

#2. четырехзначное
a = int(input("введите число: "))
if a>999 and a<10000:
    print("YES")
else:
    print("NO")

#3.
a = int(input("введите первое число: "))
b = int(input("введите вторе число: "))
c = int(input("введите ретье число: "))
if a+b>c and a+c>b and c+b>a:
    print("yes")
else:
    print("no")

#4.
a = int(input("Введите время в часах: "))
if 5 <= a <= 11:
    print("Утро")
elif 12 <= a <= 17:
    print("День")
elif 18 <= a <= 22:
    print("Вечер")
elif 23<= a < 24 or 0 <= a <= 4:
    print("Ночь")
else:
    print("Ошибка")

#5.
a = int(input("введите число: "))
if 1 <= a <= 7:
    if 1 <= a <=5:
        print("будни")
    else:
         print("выходной")

#6.
a = int(input("введите число: "))
if a<0:
    if a % 2 == 0:
        print("ОТРИЦАТЕЛЬНОЕ ЧЕТНОЕ")
elif a>0:
    if a % 2 == 0:
        print("положительное четное")
    else:
        print("положительное не четное")
else:
    print("нолик")

# ЗАДАЧИ ДЛЯ ПОДГОТОВКИ К КОНРТОЛЬНОЙ
# Задача 1.
a = int(input("введите год"))
b = a // 1000
c = (a % 1000) // 100
d = (a % 100) //10
i = (a % 10)
if (b+c+d+i)/4==0:
    print("особый кот")
else:
    print("обычный кот")