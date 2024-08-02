#Debugging in Python
#Example No 1:
#Before Debugging
def display():
    for i in range(1,10):
        if i == 10:
            print("Bye!!!")
display()             

#After Debugging
def display():
    for i in range(1,11):
        if i == 10:
            print("Bye!!!")
display()             

#Example No 2:
#Before Debugging
import random
dice_numbers = ["One","Two","Three","Four","Five","Six"]
dice_no = random.randint(1,6)
print(dice_numbers[dice_no])

#After Debugging
import random
dice_numbers = ["One","Two","Three","Four","Five","Six"]
dice_no = random.randint(0,5)
print(dice_numbers[dice_no])

#Example No 3:
#Before Debugging
year = int(input("In Which Year You Were Born?: "))
if year > 1980 and year < 1996:
    print("You are a Millenial.")
elif year > 1996:
    print("You are Gen Z")

#After Debugging
year = int(input("In Which Year You Were Born?: "))
if year > 1980 and year <= 1996:
    print("You are a Millenial.")
elif year > 1996:
    print("You are Gen Z")

#Example No 4:
#Before Debugging
age = input("How old are you?: ")
if age >= 18:
    print("You Can Vote at {age}")

#After Debugging
age = int(input("How old are you?: "))
print(type(age))
if age >= 18:
    print(f"You Can Vote at {age}")

#Example No 5:
a,b = 0,0
a = int(input("Enter a: "))
b = int(input("Enter b: "))
Multiplication = a * b
print(Multiplication)

#Example No 6:
n = int(input("Enter a No: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")    

#Example No 7:
#Before Debugging
for number in range(1,16):
    if number % 3 == 0 or number % 5 == 0:
        print("Fizzbuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print(number)

#After Debugging
for number in range(1, 16):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

