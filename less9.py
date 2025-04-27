# # 1
# names = ["Шахзодбе", "Мохирбек", "Абумалик", "Отабек", "Ёлкин"]
# for name in names:
#     print(f"Привет, {name}! Добро пожаловать в программу.")

# # 2
# names = ["Анна", "Борис", "Виктор", "Галина", "Денис"]
# count = 0
# for name in names:
#     print(f"Привет, {name}! Добро пожаловать в программу.")
#     count += 1
# print(f"Код повторился {count} раз.")


# # 3
# numbers = list(range(11, 100, 2))

# for number in numbers:
#     print(number ** 3)

# 4

films = []

for k in range(5):
    movie = input(f"Введите ваш любимый фильм №{k + 1}: ")
    films.append(movie)

print("\nФильмы:", films)