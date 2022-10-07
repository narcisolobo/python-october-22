# Pascal Case, Noun, Singular
# class is a blueprint
from tkinter.messagebox import RETRY


class Car:
    # num_cars_created = 0
    cars_created = []

    def __repr__(self):
        return f'Make: {self.make}, Model: {self.model}'

    @classmethod
    def get_num_created(cls):
        return len(Car.cars_created)

    @staticmethod
    def is_brand_new(car):
        return car.miles == 0

    # constructor function
    # runs when you create an object of this class
    def __init__(self, make, model, color, year):
        # attributes, properties, members, fields
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.miles = 0
        Car.cars_created.append(self)
    
    # instance method
    def drive(self, miles_driven):
        self.miles += miles_driven
        print('Driving...')
        return self

# get and set the values of any property using dot notation
jeep = Car('Jeep', 'Wrangler', 'Blue', 1970)
print(jeep.year)

jeep.color = 'Red'
# print(jeep.color)

jeep.drive(200).drive(25)
# print(jeep.miles)

mustang = Car('Ford', 'Mustang', 'Red', 1966)

# Test to see if we're keeping track of cars created
# for car in Car.cars_created:
#     print(car)

print(Car.get_num_created())
print(Car.is_brand_new(mustang))