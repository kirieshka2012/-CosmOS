import random
import time
import math
import datetime

print('Загрузка...')
time.sleep(1)
print('Добро пожаловать в CosmOS! Версия - 1.0')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return 'Ошибка: на 0 делить нельзя!'
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def sqrt(n):
    if n < 0:
        return 'Ошибка: нельзя извлекать корень из отрицательного числа!'
    return math.sqrt(n)

def calculator():
    while True:
        print('\nПростые операции:     Сложные операции:')
        print('1. Сложение           -1. Возведение в степень')
        print('2. Вычитание          -2. Квадратный корень')
        print('3. Умножение          ')
        print('4. Деление            ')
        print('0. Назад в меню')

        try:
            select_oper = int(input('Выберите операцию (Цифрой): '))
        except ValueError:
            print('Ошибка: введите число!')
            continue

        if select_oper == 0:
            break

        if select_oper in [1, 2, 3, 4, -1]:
            try:
                n1 = float(input('Введите первое число: '))
                n2 = float(input('Введите второе число: '))
            except ValueError:
                print('Ошибка: введите корректные числа!')
                continue

            if select_oper == 1:
                result = add(n1, n2)
            elif select_oper == 2:
                result = subtract(n1, n2)
            elif select_oper == 3:
                result = multiply(n1, n2)
            elif select_oper == 4:
                result = divide(n1, n2)
            elif select_oper == -1:
                result = power(n1, n2)

            print(f'Результат: {result}')

        elif select_oper == -2:
            try:
                n = float(input('Введите число: '))
            except ValueError:
                print('Ошибка: введите корректное число!')
                continue
            result = sqrt(n)
            print(f'Результат: {result}')

        else:
            print('Неизвестная операция. Попробуйте снова.')

def magic_number():
    while True:
        print('\nВ этой игре вам нужно угадывать число которое загадал компьютер.\n')
        try:
            min_num = int(input('Введите минимальное число: '))
            max_num = int(input('Введите максимальное число: '))
        except ValueError:
            print('Ошибка: введите число!')
            continue

        if min_num >= max_num:
            print('Ошибка: минимум не может быть больше или равен максимуму!')
            continue

        answer = random.randint(min_num, max_num)
        attemts = 0
        user_input = None
        while user_input != answer:
            attemts += 1
            try:
                user_input = int(input('Введите число: '))
            except ValueError:
                print('Ошибка: введите число!')
                continue
            
            if user_input > answer:
                print('Магическое число меньше!')
            elif user_input < answer:
                print('Магическое число больше!')
            else:
                print(f'Магическое число: {answer}\nПопыток: {attemts}')
                print('1. Заново\n2. Выход')
                while True:
                    again_exit = input('Сделайте выбор: ')
                    if again_exit == '1':
                        break
                    elif again_exit == '2':
                        return
                    else:
                        print('Ошибка: введите 1 или 2!')

def main_menu():
    while True:
        print('\nПриложения:      Игры:                   Функции:')
        print('1. Калькулятор   -1. Магическое число      +1. Время')
        print('Скоро...         Скоро...                  +2. Дата')
        print('Скоро...         Скоро...                  +3. Время и Дата')
        print('0. Выход')

        try:
            select_app = input('Выберите приложение (Цифрой): ')
        except ValueError:
            print('Ошибка: введите число!')
            continue

        if select_app == '0':
            print('\nЗавершение работы CosmOS...')
            time.sleep(1)
            break
        elif select_app == '1':
            print('\nЗапуск калькулятора...')
            time.sleep(1)
            calculator()
        elif select_app == '-1':
            print('\nЗапуск игры: Магическое число')
            time.sleep(1)
            magic_number()
        elif select_app == '+1':
            print('\nТекущее время:', datetime.datetime.now().strftime('%H:%M:%S'))
        elif select_app == '+2':
            print('\nТекущая дата:', datetime.datetime.now().strftime('%Y-%m-%d'))
        elif select_app == '+3':
            print('\nТекущая дата и время:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print('\nТакого пункта нет. Попробуйте снова.')

main_menu()