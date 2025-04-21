# What is python ? 
# Python is a programming language 
# Python is simple and easy 
# High level language 
# Developed by Guido Van Rossum 
# Python is a portable language 
# Our First Program 
print("Hello python")
print("Sohail is my name")
print("My age is 21")
# we can write this code in one line as 
print("Hello world") ,  print("I love python ") 
print("Hello , World " , "I am learning the python")
print(23)
print(23 + 35)
print("Hello" + "World")

# Variables 

# A variable is a name given to a memory location in  a program  

name = "Sohail"
age = 21
age2 = age 
price = 25.23
print(name , age2 , price )

# Rules for Identifiers

# Identifiers can be combination of uppercase and lowercase letters , digits , or an underscore
# so myVariable , varaible_1 are all valid 
# Identifier can not start with digit so while 1variable is not valid variable_1 is valid 
# we can not use symbols like !, # , % , $ 


print(type(name))
print(type(age))
print(type(price))

# Student data 
stdName = "Sohail Shoukat"
stdRoll = 12345
stdAge = 21
print("The Student name is Sohail is :" , stdName)
print("The Student Roll is :" , stdRoll)
print("The Student age is : " , stdAge)

# Data Types in Python 

# 1 Integers
# 2 String 
# 3 Float 
# 4 Boolean
# 5 None 
number1 = 31
print(number1)
print(type(number1))

# String
name1 = "SS"
name2 = 'SS'
name3 = '''SS'''
print(name1, name2 , name3)


# Boolean

isStudent = True
isTeacher = False
print(isStudent)
print(isTeacher)

# Note Python is a case sensitive language. 

num1 = 10
num2 = 10
sum = num1 + num2
print(sum)


# comments in python

# single line comments

""" Multi Line comments """

# Types of operators

# Arithemetic Operators


a = 5
b = 2 
# sum = a + b 
print(a + b)
print(a - b)
print(a * b)
print( a / b)
print( a % b) # remainder 
print( a ** b) # a^b


# Relational Operator 

a = 50 
b = 20
print(a == b) # False 
print(a != b)  # True # Sign of exlamation shows the Negative Value Not 
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)

# Assignments operators

num = 10 
num += 10
print(num)

# There are two types of conversation
# Type Conversation Automatically 
# Casting conversation  # Munually 

a = 2
b = 2.25
print(a + b)

# Castiong 
a = "2"
a = str(a)
print(type(a))
print(a)


# Input in python 

name = input("Enter the name : ")
print("Your name is : " , name  )

age = input("Enter the age ")
print("Your age is : " , age )























