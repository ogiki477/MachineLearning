# Clases in python


# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def display_details(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Course: ", self.course)


# Create a new Student object

# my_Student = Student("Ogiki Moses Odera", 3, "Software Engineering")

# # Display the Student Details
# my_Student.display_details()

# Object
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello, my name is ", self.name)
#         print("I am ", self.age, " years old")

# # Create a Person object
# my_person1 = Person("Ogiki",25)
# my_person2 = Person("Moses",35)

# # Acessing the person object attributes
# print(my_person1.name)
# print(my_person1.age)
# print(my_person2.name)
# print(my_person2.age)

# # Calling the greet method
# my_person1.greet()
# my_person2.greet()



# Exercise 1

# caclulate the area and circumference of a circle

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_area(self):
#         return 3.14 * self.radius * self.radius
#     def calculate_circumference(self):
#         return 2 * 3.14 * self.radius

# # Create a Circle object
# my_circle1 = Circle(5)
# my_circle2 = Circle(10)
# print(my_circle1.radius)
# print(my_circle2.radius)

# # calculate and display area and circumference of the circle
# print(my_circle1.calculate_area())
# print(my_circle1.calculate_circumference())
# print(my_circle2.calculate_area())
# print(my_circle2.calculate_circumference())

# Exercise 2

# Calculate and display the employee(15%) of salary (employee1: 150000,employee2: 230000)
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def calculate_employee(self):
#         return self.salary * 0.15

# # Create Employee object 
# employee1 = Employee("Ogiki", 15000)
# employee2 = Employee("Moses", 230000)

# # calculate and display the employee(15%) of salary
# print(employee1.calculate_employee())
# print(employee2.calculate_employee())


# Encapsulation 
# Importances of Encapsulation

# Encapsulation is a programming technique that hides the implementation details of an object from other objects.

# Example 4 : with a bank account

# class BankAccount:
#     def __init__(self, account_number,balance):
#         self._account_number = account_number #Encapsulates the account number attribute
#         self._balance = balance #Encapsulates the balance attribute

#     def deposit(self, amount):
#         self._balance += amount #Encapsulates the amount attribute
#     def withdraw(self,amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else:
#             print("Insufficient balance")
#     def get_balance(self):
#         return self._balance 

# # create a Bank Object
# my_account = BankAccount("12345678",1000)

# # Acess the Bank Object and modify the Bank account attributes
# print(my_account._account_number)
# print(my_account._balance)
# my_account.deposit(500)
# print(my_account._balance)
# my_account.withdraw(500)
# print(my_account._balance)


# Exercise 3  Convert 37 celcius to Fahrenheit  
     
class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius  

    def to_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit


temperature = TemperatureConverter(37)

# Convert Celsius to Fahrenheit
fahrenheit = temperature.to_fahrenheit()

# Display the result
print(f"The temperature in Fahrenheit is: {fahrenheit}°F")


# Assignment 2 : Show encapsulation with employee information to give a pay increamentation
# (Salary with employee information and to new Salary with employee information) 
# e.g from 850000 to 1000000

# Next Inheritance,polymorphism and Abstraction

