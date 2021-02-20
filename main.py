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
    l:[0,1,2,3,4,5]
    l[1] #1
    l[0:2] #[0,1] aka l[:0]
    l[2:] #[2,3,4,5]
    l[-1] #[5]
    l[::2] #[0,2,4]
    l[0:11:2] #выбрать элементы с 0 по 10 включительно с шагом 2
    l[1:-1] #выбрать все эл-ты, кроме 1 и последнего
    l[::-1] #выбрать эл-ты реверсивно
    n=3 # n!=0
    l[n:] + l[n-1:] #?


#    name = input("Hi! What are you called, Jake Sully?\n")
#    print_hi(name)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
