#Python basics

#variables
a=5
b='hello'
c=3.2
d=False


#concatenation in python
# actually we use + to concatenate
a = "Hello"
b= "Tariq"

print (a +" "+ b) #The output be will Hello Tariq


# F-strings in python
name = "Tariq"
print(f"Hello {name} how you doing") #output: Hello Tariq how you doing


# Usage of * to times the values 
print(f"{name} "* 3) #output: Tariq Tariq Tariq


#Conditional statements in python
age = input("please enter your age: ")
if age.isdigit():
    age = int(age)
    if age < 15:
        print(f"For the age of {age}, u are not qualified for the voting")
    elif age >= 15 and age <=30:
        print(f"For the age of {age}, U qualified for the voting ut still youth")
    else:
        print(f"For the age of {age} is allowed but too old")


#single conditional statement for the python programming
visualBasic = True

print(" I take visual basic programmming") if visualBasic else print("I'm   taking Information technology law")


#Lists 
items = ["bag","plate","bowl","bottle","cup","cupboard"]
#unpacking the list
print(*items) #output: bag plate bowl bottle cup cupboard


#Loops: for loop
for i in range(10):
    print(i)

fruits = ["apples","guava","mango","cherry"] #list
for fruit in fruits:
    print(fruit)

#Loops: while loop
count = 0

while count < 15:
    print("Still less than 15")
    count += 1


#functions
a = 5
b = 7

def calculate(a,b):
    return a + b

print(calculate(2,3))


#class
class Calculator:
    def __init__(self, a=None, b=None):
        """
        Initialize the Calculator class with optional values a and b.
        """
        self.a = a
        self.b = b

    def add_value(self, a, b):
        """
        Returns the sum of a and b.
        """
        return a + b

    def subtract_value(self, a, b):
        """
        Returns the difference when b is subtracted from a.
        """
        return a - b



# Example usage:
calc = Calculator()

# Using methods to perform operations
print("Addition:", calc.add_value(10, 5))        # Output: 15
print("Subtraction:", calc.subtract_value(10, 5))  # Output: 5




