#Built-in Functions
from idlelib.pyshell import usage_msg

y = max(34,56, 70, 18)
print(y)

x = min(40, 67, 34, 25)
print(x)

z = pow(2, 3)
print("The result is", z)

#User-defined functions
def greeting():
    print("Hello there!")

greeting() #Calling a Function

def multiply():
    a = 12
    b = 10
    print(a * b)

multiply()

#Parameters/variable and Arguments/value
def add(x , y):
    print(x + y)

add(4,5)
add(60,70)

def employee(fullname, age, position, status):
    print(fullname, age, position, status)

employee("Mark Joe", 54, "CEO", "Married")
employee("John Mill", 34, "HR", "Single")
employee("Sam Stan", 28, "ACCOUNTANT", "Married")
employee("Rose Kie", 31, "CLERK", "Single")







