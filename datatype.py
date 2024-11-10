
number = 67 #Integer
second = 45.98 #float
greeting ="Hello there" #string
isPythonInteresting = True # Boolean

#Dta Structures - Multiple values stored in a single variable
Cars = ["Toyota", "nissan", "vw"] #List - ordered and changeable
fruits = ("banana", "apple", "orange") #Tuple - ordered but unchangeable
country = {"Kenya", "Tunisia", "Algeria"} #set - unordered and unchangeable
student = {
    "firstname": "Jane",
    "Age" : 25,
    "course" : "Web Development",
    "gender" : "Female"
} #Dictionary - Key-value pair

print(Cars)
print(fruits)
print(country)
print(student)
print(student["gender"])


print(number)
print(second)
print(isPythonInteresting)


#Determining a datatype
print(type(country))
print(type(student))

#Typecasting
print(float(number))
print(int(second))