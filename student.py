class Student:
    def __init__(self, first_name, surname, parent_name, sex, grade, mark):
        self.first_name = first_name
        self.surname = surname
        self.parent_name = parent_name
        self.sex = sex
        self.grade = grade
        self.mark = mark

    @property
    def full_name(self) -> str:
        return self.surname + self.first_name + self.parent_name
