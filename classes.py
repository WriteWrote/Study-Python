class Student:
    _fist_name = ""
    _surname = ""
    _parent_name = ""

    _sex = ''
    _grade = -1
    _mark = -1

    def __init__(self, first_name, surname, parent_name, sex, grade, mark):
        self._fist_name = first_name
        self._surname = surname
        self._parent_name = parent_name
        self._sex = sex
        self._grade = grade
        self._mark = mark

    @property
    def get_first_name(self):
        if self._fist_name is "":
            raise Exception("Name is empty")
        else:
            return self._fist_name

    @property
    def get_surname(self):
        if self._surname is "":
            raise Exception("Surname is empty")
        else:
            return self._surname

    @property
    def get_parent_name(self):
        return self._parent_name

    @property
    def get_name(self) -> str:
        return self.get_surname + self.get_first_name + self.get_parent_name

    @property
    def get_sex(self) -> str:
        if self._sex != "M" != "F" != "М" != "Ж":
            raise Exception("Incorrect sex")
        else:
            return self._sex

    @property
    def get_mark(self) -> float:
        if self._mark < 0:
            raise Exception("Mark is < 0")
        elif self._mark > 100:
            raise Exception("Mark is > 100")
        else:
            return self._mark

    @property
    def get_grade(self) -> int:
        if self._grade < 1:
            raise Exception("Wrong grade")
        else:
            return self._grade
