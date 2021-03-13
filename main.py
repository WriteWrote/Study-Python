from student import Student


def read_from_file(name: str) -> list:
    """Reading from file to list of string and repacking string lines to objects of Student class"""
    inp_file = open(name, "r")
    result = []
    try:
        inp_str = []
        for line in inp_file:
            inp_str.append(line.strip().split("\n")[0])
        # casting
        for line in inp_str:
            values = line.split(" ")
            next_student = Student(str(values[0]), str(values[1]), str(values[2]),
                                   # surname, first name and parent name
                                   str(values[3]),  # sex
                                   int(values[4]),  # grade of student
                                   float(values[5]))  # mark of student
            result.append(next_student)
    except Exception as e:
        print(e)
    finally:
        inp_file.close()
    return result


def replace_doc(result: list, name: str):
    """Replacing old file with new values"""
    repl_file = open(name, "w")
    try:
        for stud in result:
            out_str = stud.full_name + " " + str(stud.sex) + " " + str(stud.grade) + " " + str(stud.mark)
            repl_file.write(out_str + "\n")
    except Exception as ex:
        print(ex)
    finally:
        repl_file.close()


def _grade_iter(stud_l: list, curr_grade: int, grade_arr: list):
    for stud in stud_l:
        """
        # if there is 5 or 6 grade, they will be inserted into the list of grades
        try:
            if stud.get_grade > grade_arr[-1]:
                grade_arr.append(stud.get_grade)
        except Exception as e:
            print(e)
        """
        # how python knows that there are other classes and their voids if he doesn't see them?
        if stud.grade() is curr_grade:
            yield stud


def _cut_grades(inp_list: list) -> tuple:
    """separating input list of students to several lists according to the grades"""
    result_l = []
    grade_arr = [1, 2, 3, 4]
    for grade in grade_arr:
        buff = list()
        for student in _grade_iter(inp_list, grade, grade_arr):
            buff.append(student)
        result_l.append(buff)
    return tuple(result_l)


def _weed_out_student(inp_students: list, N: int, X: float) -> list:
    # weed all students with mark < X
    weed_result = [curr_stud.mark() < X for curr_stud in inp_students]
    # delete all student with mark < X
    if len(inp_students) - len(weed_result) > N:
        inp_students = list(filter(lambda x: x.mark() < x, inp_students))
    else:
        for i in range(len(inp_students) - N):
            weed_result.pop()
        inp_students.remove(weed_result)
    return inp_students


def expel_student(inp_students: list, N: int, X: float) -> list:
    result = list()
    grades = _cut_grades(inp_students)
    for g in grades:
        result.append(_weed_out_student(list(g), N, X))
    return result


if __name__ == '__main__':
    try:
        file_name = input("Enter file name: ")
        stud_stayed = read_from_file(file_name)
        N = int(input("Enter minimum number of students left: "))
        X = float(input("Enter minimum mark: "))
        stud_stayed = expel_student(stud_stayed, N, X)
        replace_doc(stud_stayed, file_name)

    except Exception as e:
        print(e)
