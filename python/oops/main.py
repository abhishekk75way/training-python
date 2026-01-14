class Person: # Class
    def __init__(about, name, age): # Constructor
        about.name = name 
        about.age = age

    def introduce(about): # Method
        print("Hello, my name is " + about.name + " and I am " + str(about.age) + " years old")


person = Person("Abhishek Kushwaha", 22) # Object
person.introduce()

# Encapsulation
class BankAccount:
    def __init__(account, balance):
        account.__balance = balance # Private Variable - Cannot be accessed from outside the class

    def deposit(account, amount):
        account.__balance += amount # Encapsulation
        print("Deposited " + str(amount) + " rupees.")

    def withdraw(account, amount):
        if account.__balance >= amount:
            account.__balance -= amount # Encapsulation
            print("Withdrawn " + str(amount) + " rupees.")
        else:
            print("Insufficient balance.")

    def get_balance(account):
        return account.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Current balance: " + str(account.get_balance()))

# Inheritance
class Animal:
    def speak(self):
        print("Animal speaking")
    
    def sleep(self):
        print("Animal sleeping")

class Dog(Animal):
    def speak(self):
        print("Dog barking")

dog = Dog()
dog.speak()
dog.sleep()

# Polymorphism
class Cat:
    def speak(self):
        print("Cat meowing")
class Cow:
    def speak(self):
        print("Cow mooing")

for animal in [Cat(), Cow()]:
    animal.speak()

# Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")
    
    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike started")
    
    def stop(self):
        print("Bike stopped")

car = Car()
car.start()
car.stop()

bike = Bike()
bike.start()
bike.stop()