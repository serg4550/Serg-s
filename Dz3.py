class Person:
    name: str
    surname: str
    age: int

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def info_person(self):
        print(f'Person:\t{self.name} | {self.surname} | {self.age}')

class Teacher(Person):
    subject: str
    hours: int

    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        super().__init__(name=name, surname=surname, age=age)

    def info_teacher(self):
        print(f'Teacher:\t{self.subject} | {self.hours}')

    def info_all(self):
        self.info_person()
        self.info_teacher()

class Group:
    name: str
    student_count: int
    age_range: str

    def __init__(self, name: str, student_count: int, age_range: str):
        self.name = name
        self.student_count = student_count
        self.age_range = age_range

    def info_group(self):
        print(f'Group:\t{self.name} | Students: {self.student_count} | Age Range: {self.age_range}')

class Student(Person):
    progress: float
    group: Group
    pensione: bool

    def __init__(self, name: str, surname: str, age: int, progress: float, group: Group):
        super().__init__(name=name, surname=surname, age=age)
        self.progress = progress
        self.group = group
        self.set_pensione(age)

    def set_pensione(self, age: int):
        self.pensione = age >= 60

    def info_student(self):
        print(f'Student:\t{self.progress} | Group: {self.group.name} | Pensione: {self.pensione}')

    def info_all(self):
        self.info_person()
        self.info_student()

class Worker(Person):
    position: str
    duties: str
    pensione: bool

    def __init__(self, name: str, surname: str, age: int, position: str, duties: str):
        super().__init__(name=name, surname=surname, age=age)
        self.position = position
        self.duties = duties
        self.set_pensione(age)

    def set_pensione(self, age: int):
        self.pensione = age >= 60

    def info_worker(self):
        print(f'Worker:\t{self.position} | Duties: {self.duties} | Pensione: {self.pensione}')

    def info_all(self):
        self.info_person()
        self.info_worker()

# Приклади використання
group1 = Group(name='Group A', student_count=30, age_range='18-25')
student = Student(name='John', surname='Don', age=22, progress=4.5, group=group1)
student.info_all()

teacher = Teacher(subject='Python', hours=24, name='Jane', surname='Smith', age=35)
teacher.info_all()

worker = Worker(name='Mark', surname='Johnson', age=62, position='Manager', duties='Oversee operations')
worker.info_all()