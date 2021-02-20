# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}!')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #    print_hi('PyCharm')
    try:
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))

        d = b ** 2 - 4 * a * c
        if d < 0:
            print("Решение комплексное")
        elif d == 0:
            x = -b / (2 * a)
            print('Один корень: x = {:f}'.format(x))
        elif a == 0:
            print("Вы не туда попали со своим линейным уравнением")
        else:
            x1, x2 = (-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a)
            print('Два корня: x1,2 =', x1, '; ', x2)
    except ValueError:
        print('не число')
    except ZeroDivisionError:
        print('деление на 0')

#    name = input("Hi! What are you called, Jake Sully?\n")
#    print_hi(name)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
