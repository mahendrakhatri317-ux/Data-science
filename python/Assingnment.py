# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ASSIGNMENT 01 😃

# 1. Write a Python program to print your name, course, and city using proper formatting.
# Answer :
# name = "MAHENDRA KHATRI"
# course = "DATA SCIENCE IN MACHINE LEARNING"
# city = "JAIPUR"

# print("NAME : ",name)
# print("COURSE : ",course)
# print("CITY : ",city)

# output :-NAME  :  MAHENDRA KHATRI
#         COURSE :  DATA SCIENCE IN MACHINE LEARNING
#         CITY   :  JAIPUR



# 2. Take user input for name and age, then print: "Hello <name>, you are <age> years old" 
# Answer :
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print("Hello", name + ",", " you are ", age, "years old.")

# output :- Enter your name: MAHENDRA KHATRI
#           Enter your age: 19
#           Hello MAHENDRA KHATRI,  you are  19 years old.


# 3. Write a program to: 
#                   ● Take a string input  
#                   ● Print its reverse  
#                   ● Count total number of characters 

# Answer :
# string = input("Enter a string: ")
# print("Reverse of the string is: ", string[::-1])
# print("Total number of characters in the string is: ", len(string))

# output :- Enter a string: "mahendra khatri"
#           Reverse of the string is:  irtahk ardneham
#           Total number of characters in the string is:  16



# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ASSIGNMENT 02 😦

# 1. Write a program to declare variables of different data types and print them. 

# Answer : -
# name = "MAHENDRA KHATRI"               # string 
# age = 19                               # integer
# height = 5.8                           # float
# is_student = True                      # boolean


# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Is Student:", is_student)

# output :- Name: MAHENDRA KHATRI
#          Age: 19
#          Height: 5.8
#          Is Student: True


# 2. Write a program to create a string and perform operations like uppercase, lowercase, and length check.
 
# Answer : -
# string = "Hello, World!"
# print("Uppercase:", string.upper())
# print("Lowercase:", string.lower())
# print("Length of the string:", len(string))

#  output :- Uppercase: HELLO, WORLD! 
#            Lowercase: hello, world!
#            Length of the string: 13 

# 3. Write a program to create a list of numbers and print its elements using indexing.

# Answer : -
# numbers = [10, 20, 30, 40, 50]
# print("First element:", numbers[0])
# print("Second element:", numbers[1])
# print("Third element:", numbers[2])
# print("Fourth element:", numbers[3])
# print("Fifth element:", numbers[4])

# output :- First element: 10
#           Second element: 20
#           Third element: 30  
#           Fourth element: 40
#           Fifth element: 50


# 4. Write a program to concatenate two strings and store the result in a variable. 

# Answer : -
# string1 = "MAHENDRA "
# string2 = "KHATRI"
# result = string1 + string2
# print("Concatenated String:", result)

# output :- Concatenated String: MAHENDRA KHATRI


# 5. Write a program to create a list of student names and add a new name into the list.

# Answer : -
# students = ["rohit", "mahendra", "nitesh"]
# new_student = "govind bhaiya"
# students.append(new_student) 
# print("Updated list of students:", students)


# output :- Updated list of students: ['rohit', 'mahendra', 'nitesh', 'govind bhaiya']



# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ASSIGNMENT 03 😰

#  Q1. Explain Python Data Types in	detail.	Discuss	the	following data types with syntax and examples:	
#       ● 	Integer	
#       ● 	Float	
#       ● 	String	
#       ● 	Boolean	
#       ● 	List	
#       ● 	Tuple	
#       ● 	Set	
#       ● 	Dictionary	

# Answer :-
# 1. Integer: Integers are whole numbers without a decimal point. They can be positive, negative, or zero.

# Syntax: variable_name = integer_value

# Example:
# age = 25


# 2. Float: Floats are numbers that have a decimal point. They can represent both whole numbers and fractional numbers.

# Syntax: variable_name = float_value

# Example:
# height = 5.8


# 3. String: Strings are sequences of characters enclosed in quotes (single, double, or triple). They are used to represent text.

# Syntax: variable_name = "string_value"

# Example:
# name = "MAHENDRA KHATRI"


# 4. Boolean: Booleans represent one of two values: True or False. They are often used in conditional statements and logical operations.

# Syntax: variable_name = True/False

# Example:
# is_student = True

# 5. List: Lists are ordered collections of items that can be of different data types. They are mutable, meaning you can change their contents.

# Syntax: variable_name = [item1, item2, item3, ...]

# Example:
# numbers = [10, 20, 30, 40, 50]


# 6. Tuple: Tuples are ordered collections of items that can be of different data types. They are immutable, meaning you cannot change their contents after creation.

# Syntax: variable_name = (item1, item2, item3, ...)

# Example:
# coordinates = (10.0, 20.0)


# 7. Set: Sets are unordered collections of unique items. They are mutable and do not allow duplicate values.

# Syntax: variable_name = {item1, item2, item3, ...}

# Example:
# unique_numbers = {1, 2, 3, 4, 5}


# 8. Dictionary: Dictionaries are collections of key-value pairs. They are mutable and allow you to store data in a structured way.

# Syntax: variable_name = {key1: value1, key2: value2, ...}

# Example:
# student = {"name": "MAHENDRA KHATRI", "age": 19, "is_student": True}


# Q2.Write a Python	program	to demonstrate dynamic typing and	type checking using the type() function.	
#         The program should:	
#                    ● 	Declare	variables	of	multiple	data	types	
#                    ● 	Print	their	values	
#                    ● 	Print	their	corresponding	data	types	

# Answer :-
# name = "MAHENDRA KHATRI"               # string
# age = 19                               # integer
# height = 5.8                           # float
# is_student = True                      # boolean

# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Student Status:", is_student)

# print("Type of name:", type(name))
# print("Type of age:", type(age))
# print("Type of height:", type(height))
# print("Type of is_student:", type(is_student))
# print("Type of marks:", type(marks))

# output :- Name: MAHENDRA KHATRI
#           Age: 19
#           Height: 5.8
#           Student Status: True
#           Type of name: <class 'str'>
#           Type of age: <class 'int'>
#           Type of height: <class 'float'>
#           Type of is_student: <class 'bool'>


# Q3.Differentiate between Mutable and Immutable Data Types in Python with suitable examples.	
#       Also explain:	
#              ● Why strings arecimmutable	
#              ● Why lists are mutable	
#              ● Real-time use cases of	both

# Answer :-
# Mutable Data Types: Mutable data types are those that can be changed after they have been created.
# Examples of mutable data types in Python include lists, dictionaries, and sets. 

# For example, a list can be modified by adding, removing, or changing its elements:
# my_list = [1, 2, 3]
# my_list.append(4)  # my_list is now [1, 2, 3, 4]
# my_list[0] = 0    # my_list is now [0, 2, 3, 4]

# # Immutable Data Types: Immutable data types are those that cannot be changed after they have been created. 
# Examples of immutable data types in Python include strings, tuples, and frozensets. 

# For example, a string cannot be modified after it has been created : 
# my_string = "Hello"
# my_string[0] = "h"  # This will raise an error because strings are immutable

# Why strings are immutable: Strings are immutable because they are designed to be a sequence of characters that cannot be changed. 
# This immutability allows for certain optimizations in memory management and ensures that string literals can be safely shared across different parts of a program without unintended side effects.

# Why lists are mutable: Lists are mutable because they are designed to be a collection of items that can be modified. 
# This mutability allows for dynamic data structures where elements can be added, removed, or changed without needing to create a new list.

# Real-time use cases of both:
# - Immutable data types like strings are commonly used for storing and manipulating text data, such as user input, file names, and messages.
# - Mutable data types like lists are often used for collections of items that need to be modified frequently, such as a list of tasks in a to-do application, a collection of user profiles, or a set of data points in a data analysis project.  


# Q4.Write a Python	program	 to	perform	various	operations	
#         on Python collections:	
#                    ● 	List	operations	( append() 	,	 remove() 	,	slicing)	
#                    ● 	Tuple	indexing	
#                    ● 	Set	operations	(union 	, intersection )	
#                    ● 	Dictionary	operations	(keys() , values() , items() )

# Answer :-
# # List operations :-

# my_list = [1, 2, 3]
# my_list.append(4)  
# print("List after append:", my_list)       👉 Output: [1, 2, 3, 4]

# my_list.remove(2)  
# print("List after remove:", my_list)        👉 Output: [1, 3, 4]
# print("Sliced list (1:3):", my_list[1:3])   👉 Output: [3, 4]


# Tuple indexing :-

# my_tuple = (10, 20, 30)
# print("First element of tuple:", my_tuple[0])  👉 Output: 10
# print("Second element of tuple:", my_tuple[1])  👉 Output: 20
# print("Third element of tuple:", my_tuple[2])  👉 Output: 30


# Set operations :-
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1.union(set2)  
# print("Union of sets:", union_set)   👉 Output: {1, 2, 3, 4, 5}
# intersection_set = set1.intersection(set2) 
# print("Intersection of sets:", intersection_set)  👉 Output: {3}


# # Dictionary operations :-

# my_dict = {"name": "mahnendra", "age": 30, "city": "Aburoad"}
# print("Keys of the dictionary:", my_dict.keys())   👉 Output: dict_keys(['name', 'age', 'city'])
# print("Values of the dictionary:", my_dict.values())  👉 Output: dict_values(['mahnendra', 30, 'Aburoad'])
# print("Items of the dictionary:", my_dict.items())  👉 Output: dict_items([('name', 'mahnendra'), ('age', 30), ('city', 'Aburoad')])  


# Q5.Develop a mini	Student	Management System using	Python data types.	
#       The	program	should:	
#                   ● 	Store	student	details	using	Dictionary	
#                   ● 	Store	subject	marks	using	List	
#                   ● 	Calculate	total	and	average	marks	
#                   ● 	Display	the	output	in	proper	format	

# Answer :-
# student = {
#     "name": "MAHENDRA KHATRI",
#     "age": 20,
#     "subjects": ["Math", "Science", "English"]
# }
# student["marks"] = [85, 90, 78]
# total_marks = sum(student["marks"])
# average_marks = total_marks / len(student["marks"])
# print("Student Details:")
# print("Name:", student["name"])
# print("Age:", student["age"])
# print("Subjects:", student["subjects"])
# print("Marks:", student["marks"])
# print("Total Marks:", total_marks)
# print("Average Marks:", average_marks)

# output :- Student Details:
#           Name: MAHENDRA KHATRI
#           Age: 20
#           Subjects: ['Math', 'Science', 'English']
#           Marks: [85, 90, 78]
#           Total Marks: 253
#           Average Marks: 84.33333333333333

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ASSIGNMENT 04 😱

# Question 1 
# Write a program to check whether a number is: 
#                                                ● Positive 
#                                                ● Negative 
#                                                ● Zero

# Answer :-
# number = int(input("Enter a number: "))
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

# output :- Enter a number: -5
#          The number is negative.



# 2. Write a program to check whether a number is: 
#                                                 ● Even 
#                                                 ● Odd

# Answer :-
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# output :- Enter a number: 10
#           The number is even.

# 3.Write a program to check whether a student is: 
#                          ● Pass 
#                          ● Fail 
#                   (Take passing marks as 33)

# Answer :- 
# marks = int(input("Enter the marks obtained by the student: "))
# if marks >= 33:
#   print("The student has passed.")  
# else:
#   print("The student has failed.") 
  
# output :- Enter the marks obtained by the student: 45
#           The student has passed.


# 4. Write a program to check the largest number among three numbers using if-elif-else. 

# Answer :-
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("The largest number is:", num1)
# elif num2 >= num1 and num2 >= num3:
#     print("The largest number is:", num2)
# else:
#     print("The largest number is:", num3)

# output :- Enter the first number: 10
#           Enter the second number: 20
#           Enter the third number: 30
#           The largest number is: 30

# 5.Write a program to check whether a person is eligible for voting or not.  (Eligible age = 18) 


# Answer :-
# age = int(input("Enter the age of the person: "))
# if age >= 18:
#     print("The person is eligible for voting.")
# else:
#     print("The person is not eligible for voting.")

# output :- Enter the age of the person: 20
#           The person is eligible for voting.

# 6. Write a program to create a simple login system. 
#  Conditions: 
#           ● If username and password are correct → Print "Login Successful" 
#           ● Otherwise → Print "Invalid Username or Password"

# Answer :-
# correct_username = "admin"
# correct_password = "password"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == correct_username and password == correct_password:
#     print("Login Successful")
# else:
#     print("Invalid Username or Password")

# output :- Enter username: admin
#           Enter password: password
#           Login Successful


# 7. rite a program using Nested if statement for ATM withdrawal. 
#      Conditions: 
#              ● First check PIN 
#              ● Then check balance 
#              ● If both are correct → Print "Transaction Successful" 
#              ● Otherwise print proper message.
# Answer :-
# correct_pin = "1234"
# balance = 1000
# pin = input("Enter your PIN: ")
# if pin == correct_pin:
#     withdrawal_amount = int(input("Enter the amount to withdraw: "))
#     if withdrawal_amount <= balance:
#         print("Transaction Successful")
#     else:
#         print("Insufficient balance")
# else:
#     print("Invalid PIN")

# output :- Enter your PIN: 1234
#           Enter the amount to withdraw: 500
#           Transaction Successful





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ASSIGNMENT 05 😱

# 1. Create a class NumberSeries that uses a loop to print numbers from 1 to 100. 
# Answer :-
# class NumberSeries:
#     def print_numbers(self):
#         for i in range(1, 101):
#             print(i)

# obj = NumberSeries()
# obj.print_numbers()

# output :- 1
#           2
#          3
#         ...
#          100

#2. Create a class EvenOddChecker that checks and prints whether numbers from 1 to 50 are even or odd using a loop. 
# Answer :-
# class EvenOddChecker:
#   def check_numbers(self):
#         for i in range(1, 51):
#             if i % 2 == 0:
#                 print(i, "is Even")
#             else:
#                 print(i, "is Odd")

# obj = EvenOddChecker()
# obj.check_numbers()

# output :- 1 is Odd
#           2 is Even
#           3 is Odd
#          ...
#           50 is Even

# 3.	Create a class MultiplicationTable with a function to print the multiplication table of a user-given number.
# Answer :-

# class MultiplicationTable:

#     def table(self, num):
#         for i in range(1, 11):
#             print(num, "x", i, "=", num * i)

# n = int(input("Enter a number: "))

# obj = MultiplicationTable()
# obj.table(n)

# Enter a number: 5

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50

# 4. Create a class FactorialCalculator with a function to calculate the factorial of a number using a loop. 
# Answer :-
# class FactorialCalculator:

#     def factorial(self, num):
#         fact = 1

#         for i in range(1, num + 1):
#             fact = fact * i

#         print("Factorial =", fact)

# n = int(input("Enter a number: "))

# obj = FactorialCalculator()
# obj.factorial(n)

# output :- Enter a number: 5
#           Factorial = 120

# 5. Create a class PrimeNumberChecker with a function to check whether a number is prime or not. 
# Answer :-
# class PrimeNumberChecker:

#     def check_prime(self, num):

#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     print(num, "is Not Prime")
#                     break
#             else:
#                 print(num, "is Prime")
#         else:
#             print(num, "is Not Prime")

# n = int(input("Enter a number: "))

# obj = PrimeNumberChecker()
# obj.check_prime(n)

# output :- Enter a number: 7
#           7 is Prime

#6. Create a class Student with attributes: 
     #a. name 
    #b. roll number 
    #c. course 

# #answer :-
# class Student:

#     def __init__(self, name, roll_number, course):
#         self.name = name
#         self.roll_number = roll_number
#         self.course = course

#     def display(self):
#         print("Name:", self.name)
#         print("Roll Number:", self.roll_number)
#         print("Course:", self.course)


# s1 = Student("Mahendra", 101, "B.Tech")

# s1.display()

# # output :- Name: Mahendra
# #           Roll Number: 101
# #           course : B.Tech


# 7. Add a function to display student details. 
# Answer :- (Already added in the above code)
# class Student:

#     def __init__(self, name, roll_number, course):
#         self.name = name
#         self.roll_number = roll_number
#         self.course = course

#     # Function to display student details
#     def display_details(self):
#         print("Student Name :", self.name)
#         print("Roll Number  :", self.roll_number)
#         print("Course       :", self.course)


# s1 = Student("Mahendra", 101, "B.Tech")

# s1.display_details()

#output:- Student Name : Mahendra
#         Roll Number  : 101
#         Course       : B.Tech

# 8. Create a class Employee using a constructor (__init__) to store employee details and create a function to calculate yearly salary. 
# # Answer :-
# class Employee:

#     def __init__(self, name, emp_id, monthly_salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.monthly_salary = monthly_salary

#     def yearly_salary(self):
#         yearly = self.monthly_salary * 12
#         print("Employee Name :", self.name)
#         print("Employee ID   :", self.emp_id)
#         print("Yearly Salary :", yearly)


# e1 = Employee("Mahendra", 101, 25000)

# e1.yearly_salary()

# output :- Employee Name : Mahendra
#           Employee ID   : 101
#           Yearly Salary : 300000

#9. Create a parent class Person and a child class Teacher using single inheritance. Display teacher details using inherited properties. 
# Answer :-
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def display_details(self):
#         print("Teacher Name :", self.name)
#         print("Age          :", self.age)
#         print("Subject      :", self.subject)

# t1 = Teacher("Mahendra", 30, "Mathematics")
# t1.display_details()

# output :- Teacher Name : Mahendra
#           Age          : 30
#           Subject      : Mathematics

# 10. Create three classes Vehicle, Car, and SportsCar using multilevel inheritance and display information of a sports car. 
# Answer :-
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
# class Car(Vehicle):
#     def __init__(self, make, model, car_type):
#         super().__init__(make, model)
#         self.car_type = car_type
# class SportsCar(Car):
#     def __init__(self, make, model, car_type, top_speed):
#         super().__init__(make, model, car_type)
#         self.top_speed = top_speed
#    def display_details(self):
#        print("Make :", self.make)
#        print("Model :", self.model)
#        print("Car Type :", self.car_type)
#        print("Top Speed :", self.top_speed)
# s1 = SportsCar("Ferrari", "488 GTB", "Coupe", "330 km/h")
# s1.display_details()

# output :- Make : Ferrari
#           Model : 488 GTB 
#           Car Type : Coupe
#           Top Speed : 330 km/h

#11. Create a class BankAccount with functions: 
#   ● deposit money 
#   ● withdraw money 
#   ● check balance
# 
# Answer :-
# class BankAccount:
#   def __init__(self, account_holder, balance=0): 
#       self.account_holder = account_holder
#       self.balance = balance

#   def deposit(self, amount):
#       self.balance += amount

#   def withdraw(self, amount):
#       if self.balance >= amount:
#           self.balance -= amount
#       else:
#           print("Insufficient funds")

#   def check_balance(self):
#       print("Current balance:", self.balance)
# account = BankAccount("Mahendra", 1000)
# account.deposit(500)
# account.check_balance()
# account.withdraw(200)
# account.check_balance()

# output :- Current balance: 1500
#           Current balance: 1300


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ASSIGNMENT 06 😱

# # 1.Create a class NumberSeries that prints numbers from 1 to 200 using a loop.

# #answer :-
# class NumberSeries:
#     def print_numbers(self):
#         for i in range(1, 201):
#             print(i)
# obj = NumberSeries()
# obj.print_numbers()

# output :- 1
#           2
#          3
#         ...
#          200

# # 2. Create a class PrimeChecker with a function to check whether a number is prime or not.
 
# Answer :-
# class PrimeChecker:
#   def check_prime(self, num):
#       if num > 1:
#          for i in range(2, num):
#             if num % i == 0:
#                print(num, "is Not Prime")
#                break
#          else:
#             print(num, "is Prime")
#       else:

#          print(num, "is Not Prime")
# n = int(input("Enter a number: "))
# pc = PrimeChecker()
# pc.check_prime(n)

# output :- Enter a number: 11
#           11 is Prime


# # 3. Create a class Student using constructor to store: 
#  ○ name 
#  ○ roll number 
#  ○ marks 

# # Answer :-
# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def display_details(self):
#         print("Name:", self.name)
#         print("Roll Number:", self.roll_number)
#         print("Marks:", self.marks)

# # Create an object of the Student class
# s1 = Student("Mahendra", 101, 85)
# s1.display_details()

# output :- Name: Mahendra
#           Roll Number: 101
#           Marks: 85


# 4. Create a function to display student details. 
# Answer :- (Already added in the above code)
# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def display_details(self):
#         print("Name:", self.name)
#         print("Roll Number:", self.roll_number)
#         print("Marks:", self.marks)
# s1 = Student("Mahendra", 101, 85)
# s1.display_details()
# output :- Name: Mahendra
#           Roll Number: 101
#           Marks: 85



# # 5. Create a class Calculator with functions: 
#   ○ add() 
#   ○ subtract() 
#   ○ multiply() 
#   ○ divide() 

# Answer :-
# class Calculator:
#     def add(self, a, b):
#         return a + b
#     def subtract(self, a, b):
#         return a - b
#     def multiply(self, a, b):
#         return a * b
#     def divide(self, a, b):
#         if b != 0:
#             return a / b
#         else:
#             print("Error: Division by zero is not allowed.")
# calc = Calculator()
# print("Addition:", calc.add(10, 5))
# print("Subtraction:", calc.subtract(10, 5))
# print("Multiplication:", calc.multiply(10, 5))
# print("Division:", calc.divide(10, 5))

# output :- Addition: 15
#           Subtraction: 5
#           Multiplication: 50
#           Division: 2.0


# # 6. Create a parent class Person and child class Employee using single inheritance. Display employee details
# Answer :-
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Employee(Person):
#     def __init__(self, name, age, employee_id, salary):
#         super().__init__(name, age)
#         self.employee_id = employee_id
#         self.salary = salary

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Employee ID:", self.employee_id)
#         print("Salary:", self.salary)

# # Create an object of the Employee class
# emp = Employee("Mahendra", 25, "E001", 50000)
# emp.display_details()

# output :- Name: Mahendra
#           Age: 25
#           Employee ID: E001
#           Salary: 50000


# # 7.Create a class BankAccount with functions: 
#   ○ deposit() 
#   ○ withdraw() 
#   ○ check_balance() 

# Answer :-
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Error: Insufficient funds.")
#     def check_balance(self):
#         print("Current balance:", self.balance)
# account = BankAccount("Mahendra", 1000)
# account.deposit(500)
# account.withdraw(200)
# account.check_balance()

# output :- Current balance: 1300



# # 8.Create a class FactorialCalculator with a function to calculate factorial of a number using a loop. 
# # Answer :-
# class FactorialCalculator:

#     def factorial(self, num):

#         fact = 1

#         for i in range(1, num + 1):
#             fact = fact * i

#         print("Factorial of", num, "is", fact)


# n = int(input("Enter a number: "))

# obj = FactorialCalculator()
# obj.factorial(n)

# output :- Enter a number: 4
#           Factorial of 4 is 24






# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> python assignment complete ✔