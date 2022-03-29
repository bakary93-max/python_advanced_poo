# exercise 1
import string, random


class Book:
    price = 9.99

    # initialise an instance
    def __init__(self, price):
        # create an instance attribute
        self.price = price

    def change_price(self, price):
        self.price = price


# create an instance
harry_potter = Book(19.99)


class Company:
    employees = []


class Employee:
    def __init__(self, firstname, lastname, position, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.salary = salary

    # for changing instance representation
    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


john = Employee("John", "Smith", "Python Developer", 45000)
# print(john)
employees = [("John", "Smith", "Python Developer", 45000),
             ("Bakary", "Sane", "Python Developer", 47000),
             ("Saliou", "FAYE", "Python Developer", 55000),
             ("Awa", "Badiane", "Python Developer", 5500),
             ("Amaye", "Sambou", "Developer", 5500)]

for employee_data in employees:
    employee = Employee(*employee_data)
    Company.employees.append(employee)
    # print(employee)


class ListCustom(list):
    pass


liste = ListCustom()
liste.append(5)


class Cube:
    def __init__(self, x=5, y=2, z=7):
        self.x = x
        self.y = y
        self.z = z

    def move_x(self):
        self.x += 1


my_cube = Cube()
my_cube.move_x()


class Car:
    def __init__(self, marque, price=0):
        self.marque = marque
        self.price = price

    def __repr__(self):
        return f"{self.marque} {self.price}"

    def change_price(self, price):
        if isinstance(price, int):
            self.price = price


car = Car(marque="Toyota", price=20)
car.change_price(2344)


# print(car)


class Human:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Magician(Human):
    def __init__(self, firstname, lastname):
        super().__init__(firstname=firstname, lastname=lastname)
        self.power = 80


class Gobelan(Human):
    def __init__(self, firstname, lastname):
        super().__init__(firstname=firstname, lastname=lastname)
        self.power = 20


class Chevalier(Human):
    def __init__(self, firstname, lastname):
        super().__init__(firstname=firstname, lastname=lastname)
        self.power = 70


class MachineACafe:
    def __init__(self):
        self.temperature_eau = 0

    def __chauffe_eau(self):
        self.temperature_eau = 100
        print("L'eau est chaude")

    def __moud_cafe(self):
        print("Cafe moulu avec succes")

    def fait_du_cafe(self):
        self.__moud_cafe()
        self.__chauffe_eau()
        print("Le cafe est prêt")


# machine = MachineACafe()
# machine.fait_du_cafe()


class Chanson:
    paroles = """Joyeux anniversaire,
Joyeux anniversaire,
Joyeux anniversaire {prenom},
Joyeux anniversaire."""

    @staticmethod
    def chante_pour(prenom):
        return Chanson.paroles.format(prenom=prenom)


Chanson.chante_pour(prenom="Paul")

etudiants_partis = []


class Etudiant:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __del__(self):
        etudiants_partis.append('{} {}'.format(self.firstname, self.lastname))


bakary = Etudiant("Bakary", "Sane")
baka = Etudiant("Baka", "Sene")

del baka


# print(etudiants_partis)


class Count:
    def __init__(self, firstname, number, balance):
        self.firstname = firstname
        self._number = number
        self.balance = balance
        self.payments = {}

    def __repr__(self):
        return f"{self.firstname} {self.balance} {self.payments}"

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self.number = value
        # raise AttributeError("You cannot modify the count number")

    def deposit(self, amount):
        self.balance += amount
        iud = "".join(random.sample(string.digits + string.ascii_letters, 15))
        self.payments[iud] = amount

    def retire(self, amount):
        self.balance -= amount


count_bakary = Count(firstname="Bakary", number=1, balance=1)
count_bakary.deposit(amount=8)


# print(count_bakary)


# count_bakary.retire(amount=3)
# print(count_bakary)


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Je ne sais pas quoi dire...")


class Dog(Animal):
    def talk(self):
        return "Woof!"


class Cat(Animal):
    def talk(self):
        return "Miaou!"


a = Animal("Patrick")
cat = Cat("Titi")
dog = Dog("Max")


# print(cat.talk())
# print(dog.talk())


class Study:
    directory = []

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.uid = len(Study.directory) + 1
        Study.directory.append(self)


bakaryy = Study("Bakary", "Sane")
marc = Study("Marc", "Tremblay")


# print(Study.directory)


# An example of contextmanager for using with instruction
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # called at the entrance of the context
    def __enter__(self):
        print("The area of the triangle of {}m by {}m is :".format(self.
                                                                   width, self.length))
        return self

    # called when exiting the context
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("{}m2".format(self.area))

    def calculate_area(self):
        self.area = self.length * self.width


with Rectangle(6, 12) as r:
    r.calculate_area()


class Email:
    number_of_mails_sent = 0

    def __init__(self, content):
        self.content = content
        self.is_sent = False

    def send_to(self, email):
        if not self.is_sent:
            self.is_sent = True
            Email.number_of_mails_sent += 1
            return "Email sent"
        return "Email already sent"


email = Email(content="Hello Bakary!")
email.send_to(email="saneb2580@gmail.com")


class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Classes:
    students_list = []

    @staticmethod
    def add_student(firstname, lastname):
        student = Student(firstname=firstname, lastname=lastname)
        Classes.students_list.append(student)


Classes.add_student("Bakary", "Sane")


# print(Classes.students_list)


class Pizza:
    def __init__(self, name, ingredients, price=9.99):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __repr__(self):
        return f"{self.name} {self.price} {self.ingredients}"

    @classmethod
    def neapolitan(cls):
        print(cls(name="Pizza Neapolitan", ingredients=["Tomatoes", "Anchovies"], price=12.99))

    @classmethod
    def cheese(cls):
        print(cls(name="3 cheeses", ingredients=["Mozzarella", "County, Cheddar"], price=13.99))


# Pizza.neapolitan()
# Pizza.cheese()


# password generator
class PasswordGenerator:

    @staticmethod
    def generate(length):
        return "".join(random.sample(string.digits + string.ascii_letters, length))


password = PasswordGenerator.generate(15)
# print(password)


class Note:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}/20"


class Notes(list):
    def add_notes(self, mark):
        self.append(mark)

    def perfects_notes(self):
        number = 0
        for mark in self:
            if mark.value == 20:
                number += 1
        return number

    def mean(self):
        sum = 0
        for mark in self:
            sum += mark.value
        return sum / len(self)

        # return round(sum([mark.value for mark in self])/len(self), 1)


value_notes = [13, 14, 20, 5, 20, 17, 20]
note = Notes()

for value_note in value_notes:
    note.add_notes(mark=Note(value=value_note))

# print(note.perfects_notes())
# print(note.mean())


class Path:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def __add__(self, content):
        return Path(self.path + "/" + content)


c = Path("/Users/bakary")
composite = c + "dossier" + "test" + "script"
#print(composite)
