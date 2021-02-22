# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}!')  # Press Ctrl+F8 to toggle the breakpoint.


def func(list: List[float]):
    # map for counting numbers
    map = {}

    for currEl in list:
        if currEl not in map:
            map[currEl] = 0
        map[currEl] += 1

    # turning map into list of entries?
    map = [(v, k) for v, k in map.items()]
    map.sort(key=lambda k: (-k[1], k[0]))
    # finally getting list as result

    # why do not working "result = list()"?
    # changes to "result = list"
    result = []
    for value in map:
        for i in range(0, value[1]):
            result.append(value[0])

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    str = None
try:
    # get input and trim spaces in the end
    str = input('enter values:\n').strip()
    # casting float
    l = [float(x) for x in str.split(' ')]
    # print(l)
    result = func(l)
    print(result)
except ValueError:
    print("Wrong type of arguments")
