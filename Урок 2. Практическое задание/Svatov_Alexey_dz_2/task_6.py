"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

from random import randint


def game_rand(try_n, n=randint(0, 100), count=1):
    if try_n == n:
        return print('Вы угадали!')
    elif count == 10:
        return print(f'Вы не угадали за 10 попыток. Загаданное число = {n}')
    else:
        return game_rand(int(input('Ваше число больше загаданного. Попробуйте еще раз: ')), n,
                         count + 1) if try_n > n else game_rand(
            int(input('Ваше число меньше загаданного. Попробуйте еще раз: ')), n, count + 1)


game_rand(int(input('Число загадано.Введите Ваш вариант: ')))
