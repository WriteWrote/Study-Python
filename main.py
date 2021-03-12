from classes import Student


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
                                   # first name, surname and parent name
                                   str(values[3]),  # sex
                                   int(values[4]),  # grade of student
                                   float(values[5]))  # mark of student
            result.append(next_student)
    except Exception as e:
        print(e)
    finally:
        inp_file.close()
    return result


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
        if stud.get_grade() is curr_grade:
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


if __name__ == '__main__':
