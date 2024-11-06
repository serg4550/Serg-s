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


# Введення даних з клавіатури
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

# Створення групи
group = Group(name=group_name, age_range=age_range, students=students)

# Виведення інформації про групу
group.info_group()