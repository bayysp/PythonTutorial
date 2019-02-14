class Student():
    def __init__(self, Name):  # this is an constructor
        self._Name = Name

    def getNameStudent(self):
        print("Student Name is", self._Name)


def main():
    student = Student("Bayu Saputra")  # send a value to constructor in class Student

    student.getNameStudent()


if __name__ == '__main__':
    main()
