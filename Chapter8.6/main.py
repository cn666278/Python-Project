class Dog():
    def __init__(self, name, age):
        self.name = name;
        self.age = age

    def sit(self):
        print(self.name.title() + " in now sitting.")

    def rolling(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('wangcai',6)
print("My dog name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# invoke method in class
my_dog.sit()
my_dog.rolling()

print("\n")

# Declare another class sample
your_dog = Dog('goudan',3)
print("Your dog name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.rolling()


#  a new class
# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + " " + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer:
#             self.odometer = mileage
#         else:
#             print("You can not roll back an odometer")
#
#
# my_new_car = Car('BMW', 'I8', 2021)
# print("My new car is : " + my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(10000)
# my_new_car.read_odometer()


# Inheritance
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can not roll back an odometer")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + "-kWh battery.")

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

my_tesla = ElectricCar('tesla', 'model s', 2021)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Python Standard Library
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['John'] = 'python'
favorite_languages['Alaska'] = 'c'
favorite_languages['Sam'] = 'C++'
favorite_languages['Queen'] = 'java'

for name, language in favorite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")