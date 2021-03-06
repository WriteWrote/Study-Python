# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def m_iter(m):
    i = 0
    j = 0
    d = 1

    for j in range(len(inp_array) + 1):
        for i in range(j):
            if (j % 2 == 0):
                yield inp_array[j - i - 1][i]
            else:
                yield inp_array[i][j - i - 1]

    for j in range(len(inp_array) - 1, -1, -1):
        for i in range(j - 1, -1, -1):
            if (j % 2 != 0):
                yield inp_array[j - i + (len(inp_array) - j - 1)][len(inp_array) - (j - i)]
            else:
                yield inp_array[len(inp_array) - (j - i)][j - i + (len(inp_array) - j - 1)]


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

        l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        for x in m_iter(l):
            print(x)

        # the key element of task
        result, seq = check_array(inp_array)
        print(result, seq)

    except FileNotFoundError:
        print("No such file")
    except Exception as e:
        print(e)
