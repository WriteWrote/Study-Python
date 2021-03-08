# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def m_iter(m: list):
    for j in range(len(m) + 1):
        for i in range(j):
            if j % 2 == 0:
                yield m[j - i - 1][i]
            else:
                yield m[i][j - i - 1]

    for j in range(len(m) - 1, -1, -1):
        for i in range(j - 1, -1, -1):
            if j % 2 != 0:
                yield m[j - i + (len(m) - j - 1)][len(m) - (j - i)]
            else:
                yield m[len(m) - (j - i)][j - i + (len(m) - j - 1)]


def check_array(arr: list) -> tuple:
    res = False
    seq = []  # for sequence

    prev_el = None
    for x in m_iter(arr):
        # safe-point to avoid None
        if prev_el is None:
            prev_el = x
        # check if there is ++ / -- sequence
        else:
            if (x == prev_el + 1) or (prev_el - 1 == x):
                res = True
            else:
                res = False
        # change prev_el
        prev_el = x

    # return tuple
    return res, seq


if __name__ == '__main__':
    try:
        # read from file
        inp_file = open("input2.txt", "r")
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

        for x in m_iter(inp_array):
            print(x)

        # the key element of task
        result, seq = check_array(inp_array)
        print(result, seq)

    except FileNotFoundError:
        print("No such file")
    except Exception as e:
        print(e)
