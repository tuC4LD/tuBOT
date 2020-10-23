import random

from colorama import Fore
from colorama import init
from pyowm import OWM
from pyowm.utils.config import get_default_config

init()

active = True
owm = OWM('7b11468180a49db8c71e441c84f430d4')
mgr = owm.weather_manager()


def console_picture():
    print(Fore.CYAN)
    print("                **    **  ********  **        **            **      ")
    print("               **    **  ********  **        **         **     **   ")
    print("              ********  **        **        **         **      **  ")
    print("             ********  ********  **        **         **      **  ")
    print("            **    **  **        **        **         **      **  ")
    print("           **    **  ********  ********  ********    **    **   ")
    print("          **    **  ********  ********  ********       **      ")


console_picture()
print(Fore.YELLOW)
print("Вас приветствует многофункциональный ассистент tuBOT V2.0 by Фёдор Фролов 7Т")
print("Данная программа умеет определять погоду, считать, а также играть в разные встроенные игры")
print("На данном этапе разработки есть такие игры как:")
print("1. Угадай число")
print("2. Орёл и Решка (Beta)")
print("Больше игр появится несколько позже")
input("Чтобы начать нажмите ENTER")
print("")


def func_list():
    print("1. Калькулятор [C]")
    print("2. Погодник [W]")
    print("3. Угадай число [M]")
    print("4. Орёл И Решка [R]")
    print("Выйти из программы [N]")


func_list()
print(Fore.RED)

res = input("Выберите функцию: ")

while active:
    print(Fore.WHITE)

    if res == "W":
        place = input('Для начала выберете насёленный пункт в котором хотите узнать погоду: ')
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        observation = mgr.weather_at_place(place)
        w = observation.weather
        weather = w.temperature('celsius')["temp"]
        weather2 = w.wind()["speed"]
        print(Fore.CYAN)
        print("В городе ", place, " сейчас " + w.detailed_status)
        print(Fore.GREEN)
        print("Температура в районе " + str(weather))
        print(Fore.RED)
        print("Скорость ветра " + str(weather2) + "М/С")
        print(Fore.YELLOW)
        print("Влажность воздуха в районе " + str(w.humidity) + "%")
        print(Fore.WHITE)
        res = input("Выберете функцию: ")

    elif res == "N":
        active = False
        print("До свидания")

    elif res == "M":
        number = random.randint(1, 20)
        print(Fore.CYAN)
        running = True

        while running:
            print("Загаданное число не больше 20 и не 0")
            guess = int(input("Введите целое число или [0] чтобы выйти: "))
            if guess == number:
                print("Поздравляю, вы угадали.")
                running = False
                print(Fore.WHITE)
                func_list()
                res = input("Выберите функцию: ")

            elif guess == 0:
                print("Игра Закрыта!")
                res = "0-0-0"
                break

            elif guess < number:
                print("Нет, загаданное число немного больше этого")

            else:
                print("Нет, загаданное число немного меньше этого. ")

    elif res == "c":
        print(Fore.GREEN)

        what = input("Чё делать будем? (+, -, /, *): ")

        print(Fore.CYAN)

        a = float(input("Введи первое число: "))
        b = float(input("Введи второе число: "))

        print(Fore.YELLOW)

        if what == "+":
            c = a + b
            print("Результат: " + str(c))
            print(Fore.WHITE)
            func_list()
            res = input("Выберите функцию: ")

        elif what == "-":
            c = a - b
            print("Результат: " + str(c))
            print(Fore.WHITE)
            func_list()
            res = input("Выберите функцию: ")

        elif what == "/":
            c = a / b
            print("Результат: " + str(c))
            print(Fore.WHITE)
            func_list()
            res = input("Выберите функцию: ")

        elif what == "*":
            c = a * b
            print("Результат: " + str(c))
            print(Fore.WHITE)
            func_list()
            res = input("Выберите функцию: ")
        else:
            print("Нормальную операцию выбери, окей?")
            func_list()
            res = input("Выберите функцию: ")

    elif res == "0-0-0":
        func_list()
        res = input("Выберите функцию: ")

    elif res == "R":
        print(Fore.GREEN)
        input("Чтобы подкинуть монетку нажмите ENTER")
        monetka = ["Орёл", "Решка"]
        cva = random.choice(monetka)
        print("Выпало:", cva)
        print(Fore.WHITE)
        func_list()
        res = input("Выберите функцию: ")

    elif res == "G":
        print("Ты Лох")

    else:
        func_list()
        res = input("Выберите корректную функцию!: ")

input()
