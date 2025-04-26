# operators_keywords _variables.

x = 5 
y = -x
print(type(y))
print(y)

a = False
b = not a 
print(b)



# Binary-Operators

# Arithmetic Operators + , - , * , / , ** , % 

a = 5
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print( a % b)


# Comparison Operators # Relational 

x = 5;
y = 5;
print(x == y )
print(x != y)
print(x <= y)
print(x >= y )


# Logical Operators 

a = 30 > 20 and 20 > 10
print(a)
b = 5 > 3 or 3 < 5

# walrus operator

if (n := len([1, 2, 3, 4])) > 3:
    print(f"List bohot lambi hai, {n} items hain.")
 # conditional statements 


age = 21
if(age >=18):
        print("Can vote and apply for driver license ")

# light = "red"

light = str(input("Enter the traffic light : "))
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "look"):
    print("look")
else:
    print("Light is broken")


x = 10
if(x >=5):
 
 print("10 is greater than 5 " )

 age = 14
 if(age >= 18):
     print("Able for vote")
 else: 
     print("Can not")


marks = int(input("Enter your marks : "))

if(marks >= 90):
    Grade = "A"
elif(marks >=80 and marks < 90):
    Grade = "B"
elif(marks >=70 and marks < 60):
     Grade = "C"
else : 
    Grade = "D"
    print("You got", Grade)


#  Identity Operators

a = [1 , 2 , 3 ]
b = a 
print(a is b ) 


a = [1 , 2 , 3 ] 
b = [1 , 2 , 3 , 4 ] 
print(a is not b ) 

# Valid variable names 
name = "sohail"
_age = 21
salary2024 = 50000
my_var = "python"

print(name , _age , salary2024 ,my_var)












