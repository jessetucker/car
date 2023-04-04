# Program: car.py
# Author: Jesse Tucker III
# Date April 2023

# The Car class initializes attributes of a car and increase or decrease
# it's speed.

class Car:
    # The __init__ method initializes the data attributes
    # __year_model, __make, and __speed.

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # The accelerate method increments the __speed attribute by 5.

    def accelerate(self):
        self.__speed += 5
    
    # The brake method decrements the __speed attribute by 5.

    def brake(self):
        self.__speed -= 5
    
    # The get_speed method returns the current speed.

    def get_speed(self):
        return self.__speed

# The main function creates a car object that accelerates and decelerates
# the cars speed.

def main():
    # Creates an object car1 of the Car class that accepts two parameters

    car1 = Car(2023, 'Ford F-350 Super Duty')

    # Acclerate car1 object and display the current speed five times.

    for num in range(5):
        car1.accelerate()
        print(car1.get_speed())
    
    # Decelerate car1 object and display the current speed five times.

    for num in range(5):
        car1.brake()
        print(car1.get_speed())

# Call the main function.

main()
