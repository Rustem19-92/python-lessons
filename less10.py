cars = ['toyota', 'Mazda', 'Hyundai', 'GM', 'Kia']

for car in cars:
    if car.upper() == 'GM':
        print(car.upper())
    else:
        print(car.capitalize())
# ------
username = input("Введите ваше имя пользователя: ")

if username.lower() == 'admin':
    print("Добро пожаловать, admin. Вы видите список пользователей?")
else:
    print(f"Добро пожаловать, {username}!")


# ------
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if num1 == num2:
    print("Числа равны.")

number = float(input("Введите число: "))

# ------
if number < 0:
    print("Отрицательное число.")
elif number > 0:
    print("Положительное число.")
else:
    print("Число равно нулю.")

# -----

import math

number = float(input("Введите число: "))
if number >= 0:
    root = math.sqrt(number)
    print(f"Квадратный корень числа {number} равен {root}.")
else:
    print("Введите положительное число.")