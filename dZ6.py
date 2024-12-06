import inspect

# Класси StudySubject, Student и Group
class StudySubject:
    def __init__(self, name: str, hours: int, enable: bool):
        self.name = name
        self.hours = hours
        self.enable = enable

    def info_study(self):
        print(f'Study: {self.name} | Hours: {self.hours} | Enabled: {self.enable}')


class Student:
    def __init__(self, name: str, surname: str, subjects: list):
        self.name = name
        self.surname = surname
        self.subjects = subjects

    def info_student(self):
        print(f'Student: {self.name} | Surname: {self.surname}')

    def info_all(self):
        self.info_student()
        for subject in self.subjects:
            subject.info_study()


class Group:
    def __init__(self, name: str, age_range: str, students: list):
        self.name = name
        self.age_range = age_range
        self.students = students

    def info_group(self):
        print(f'Group: {self.name} | Student Count: {len(self.students)} | Age Range: {self.age_range}')
        for student in self.students:
            student.info_student()


# Ввод данных с клавиатуры
group_name = input("Enter group name: ")
age_range = input("Enter age range: ")

students = []
while True:
    name = input("Enter student name (or 'exit' to finish): ")
    if name.lower() == 'exit':
        break
    surname = input("Enter student surname: ")

    subjects = []
    while True:
        subject_name = input("Enter subject name (or 'done' to finish): ")
        if subject_name.lower() == 'done':
            break
        hours = int(input(f"Enter hours for {subject_name}: "))
        enable = input(f"Is {subject_name} enabled? (yes/no): ").lower() == 'yes'
        subjects.append(StudySubject(name=subject_name, hours=hours, enable=enable))

    students.append(Student(name=name, surname=surname, subjects=subjects))

# Создание группы
group = Group(name=group_name, age_range=age_range, students=students)

# Вывод информации о группе
group.info_group()


# Классы Person, Student и Worker
class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        return f'Name: {self.name}, Surname: {self.surname}, Age: {self.age}'


class Student(Person):
    def __init__(self, name: str, surname: str, age: int, subjects: list):
        super().__init__(name, surname, age)
        self.subjects = subjects

    def info_student(self):
        return f'Student Info: {self.info()} | Subjects: {", ".join([subject.name for subject in self.subjects])}'


class Worker(Person):
    def __init__(self, name: str, surname: str, age: int, position: str):
        super().__init__(name, surname, age)
        self.position = position

    def info_worker(self):
        return f'Worker Info: {self.info()} | Position: {self.position}'


# Инспекция классов Student и Worker
print("\nИнспекция класса Student:")
student_attributes = [attr for attr in dir(Student) if not callable(getattr(Student, attr)) and not attr.startswith("__")]
student_methods = [method for method in dir(Student) if callable(getattr(Student, method)) and not method.startswith("__")]

print("Атрибуты:", student_attributes)
print("Методы:", student_methods)

print("\nИнспекция класса Worker:")
worker_attributes = [attr for attr in dir(Worker) if not callable(getattr(Worker, attr)) and not attr.startswith("__")]
worker_methods = [method for method in dir(Worker) if callable(getattr(Worker, method)) and not method.startswith("__")]

print("Атрибуты:", worker_attributes)
print("Методы:", worker_methods)