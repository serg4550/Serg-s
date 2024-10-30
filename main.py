# задание 1
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 100  # Уровень счастья кота
        self.energy = 100     # Уровень энергии котика

    def feed(self):
        self.happiness += 10
        self.energy += 5
        print(f"{self.name} был накормлен. Уровень счастья: {self.happiness}, Энергия: {self.energy}")

    def play(self):
        if self.energy >= 20:
            self.happiness += 20
            self.energy -= 20
            print(f"{self.name} играет. Уровень счастья: {self.happiness}, Энергия: {self.energy}")
        else:
            print(f"{self.name} слишком устал для игры.")

    def rest(self):
        self.energy += 30
        print(f"{self.name} отдыхает. Энергия: {self.energy}")

    def status(self):
        print(f"{self.name} ({self.species}) - Счастье: {self.happiness}, Энергия: {self.energy}")
#задание 2
class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100  # Начальные деньги
        self.studying = False
        self.working = False

    def work(self):
        if not self.working:
            self.working = True
            self.money += 50  # Заработок
            print(f"{self.name} работает и зарабатывает деньги. Текущие деньги: {self.money}")
        else:
            print(f"{self.name} уже работает.")

    def study(self):
        if self.studying:
            print(f"{self.name} уже учится.")
        else:
            self.studying = True
            print(f"{self.name} начинает учиться.")

    def rest(self):
        if self.money > 0:
            self.money -= 10  # Траты во время отдыха
            print(f"{self.name} отдыхает. Текущие деньги: {self.money}")
        else:
            print(f"{self.name} не хватает денег, чтобы отдохнуть. Нужно работать.")

    def status(self):
        print(f"{self.name} - Деньги: {self.money}, Учится: {self.studying}, Работает: {self.working}")

    def live_year(self):
        for month in range(12):
            print(f"Месяц {month + 1}:")
            if self.money < 20:
                self.work()
            elif self.studying:
                self.rest()
            else:
                self.study()
# Создание питомца
my_pet = Pet("Мурзик", "Кот")
my_pet.feed()
my_pet.play()
my_pet.rest()
my_pet.status()

# Создание студента
student = Student("Алексей")
student.status()
student.work()
student.rest()
student.live_year()