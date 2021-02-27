# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def check_array(input_array):
    checkpoint = len(input_array)
    for x in range(len(input_array)):

    return False
"""

if __name__ == '__main__':
    try:
        # read from file
        arr_file = open("input.txt", "r")
        try:
            input_str = []
            for line in arr_file:
                input_str.append(line.strip().split("\n")[0])
            # casting
            input_array = []
            for line in input_str:
                input_array.append([float(x) for x in line.split(' ')])
            # checking
            print(input_array)
        except Exception as e:
            print(e)
    except FileNotFoundError:
        print("No such file")
