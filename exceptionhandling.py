try:
    number = 3
    print(number)

except:
    print("An error has occurred")

num1 = 45
num2 = 0
try:
    num1 = 45
    num2 = 0
    print(num1 / num2)

except:
    print("A zero division error has occurred")
finally:
    print("Success")