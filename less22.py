# --------------------1--------------------
# * - args метод


def multiplication(*numbers):
    """Функция, которая вычисляет умножение входных чисел"""
    multiplic = 1
    for number in numbers:
        multiplic *= number
    return multiplic

print(multiplication(2,3,4,5,6))

# --------------------2------------------------
# ** - kwargs метод

def student_info(name,surname,**info):
    """Функция, которая возвращает информацию о студенте в виде словаря"""
    info['name'] = name
    info['surname'] = surname
    return info

info = student_info('Rustem', 'Rakhmanov', birth=1992, place='Tashkent', university='Harward', direction='IT')
print(info)