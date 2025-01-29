class Student:
    def __init__(self, name, gender, age, s_id):
        self.name = name
        self.gender = gender
        self.age = age
        self.s_id = s_id

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_s_id(self):
        return self.s_id

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age

    def set_s_id(self, s_id):
        self.s_id = s_id


def create_student():
    name = input("Enter name: ")
    gender = input("Enter gender: ")
    age = int(input("Enter age: "))
    s_id = input("Enter student ID: ")
    return Student(name, gender, age, s_id)


student = create_student()
print(f"Student Name: {student.get_name()}")
print(f"Student Gender: {student.get_gender()}")
print(f"Student Age: {student.get_age()}")
print(f"Student ID: {student.get_s_id()}")