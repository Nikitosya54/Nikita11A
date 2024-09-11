#1 задача
num1 = int(input("введите первое число: "))
num2 = int(input("введите вторе число: "))

if num1 == num2:
    print ("числа одинаковые")
else:
    print ("числа не равные")
#2 задача
num1 = int(input("введите первое число: "))
num2 = int(input("введите вторе число: "))

if num2 != 0:
    if num1 % num2 ==0:
        print(f"{num1} делится на {num2} БЕЗ остатка")
    else:
        print(f"{num1} делится на {num2} С остатком")

