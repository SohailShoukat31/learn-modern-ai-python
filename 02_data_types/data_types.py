print("Hello Python")
# 1 Numeric 
# Python has three main numeric types:

# a. Integer (int)
num_int = 42
print(type(num_int))
print(num_int)

# b. Floating-Point (float)

num_float = 3.14
print(type(num_float))
print(num_float)

# c. Complex (complex)
num_complex = 2 + 3j 
print(type(num_complex))
print(num_complex)

# Attrribute Real and Imag

z = 4 + 3j 
print(type(z))
print(z.real)
print(z.imag)

x = -6 + 8j 
print(x.real + z.imag)

z = 10 - 3j 
print(z.imag)


y = 4 + 3j
print(type(y))


# 2. Boolean (bool)

isStudent = True
isTeacher = False 
print(isStudent)
print(isTeacher)


# 3. Sequence Types

# a. String (str)

text_single = 'Hello python !'
text_double = "Hello python !"
text_triple = '''Hello python !'''
print(type(text_single))
print(text_single , text_double , text_triple)

# b. List (list)

my_list = [1 , 2 , 3 , "Python" , True , 3 + 4j ]
print(my_list)
print(type(my_list))

# c. Range (range)

num_range = range(1 , 2 , 3) # range(start, stop, step)
print(num_range)
print(num_range.start)
print(num_range.stop)
print(num_range.step)


name = input("Enter the name :")
age =  int(input("Enter the age  :"))
marks = float(input("Enter the marks :"))
print("Welcome :", name)
print("age :" ,age)
print("marks : " , marks)

# Lets Practice 

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the seconfd number "))
print(num1 + num2)


side = float("enter the side ")
print("Area of side is :" ,  side * side )

# String
# String is a data type  that stores of a sequence of characters

# String 
str1 = "Sohail"
str2 = 'Python'
str3 = '''I love python'''
print(str1 , str2 , str3)

next_line = "This is string.\nwe are creating it in pyhon"
print(next_line)

# Basic Operations 
# Concatenation 
str1 = "Hello"
str2 = "World"
final_str = str1 + str2
print(final_str)

# lenght of string 

name = "Apni Python"
print(len(name))
print(name[3])
print(name)


slicing_value = "Karachi"
print(slicing_value[2:5])


# String Function 

# 1 endswith()
str = "I am studying python from GIAIC"
print(str.endswith("AIC")) # True

str2 = "I love my python language"
print(str2.endswith("ugf")) # False 

# 2 capitalize()

str = "sohail"
print(str.capitalize())

#  3 Replace()

str = "I am learning python"
print(str.replace("python" , "C++"))


user_name = input("Enter your name ")
print(user_name)
print("The lenght of the username is : " , len(user_name))



