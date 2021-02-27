# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def check_array(input_array):
    res = False
    seq = []  # for sequence

    checkpoint = len(input_array)
    for x in range(len(input_array)):
        res = True
    # return tuple
    return res, seq


if __name__ == '__main__':
    try:
        # read from file
        inp_file = open("input.txt", "r")
        inp_array = []
        try:
            inp_str = []
            for line in inp_file:
                inp_str.append(line.strip().split("\n")[0])
            # casting
            for line in inp_str:
                inp_array.append([float(x) for x in line.split(' ')])
            # checking
            print(inp_array)
        except Exception as e:
            print(e)
        finally:
            inp_file.close()

        # the key element of task
        result, seq = check_array(inp_array)
        print(result, seq)
    except FileNotFoundError:
        print("No such file")
    except Exception as e:
        print(e)
