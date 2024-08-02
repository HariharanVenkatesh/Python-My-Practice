#Nested if Else & elif

a = 52
if a % 2 == 0:
    print("Even")
    if (a > 30):
        print("Number is Greater than 30 ")
print("Bye")   

a = 51
if a % 2 == 0:
    print("Even")
    if (a > 30):
        print("Number is Greater than 30 ")
print("Bye")   


#Nested if&Else Condition
height = int(input("What is your height? "))

if height> 3:
    print("You can able to ride")
    age=int(input("What is your age? "))
    if age<=18:
        print("Please pay 250 Rs/-")
    else:
        print("Please pay 500 Rs/-")
else:
    print("can't ride")
print("bye")

#elif Condition

height = int(input("What is your height? "))

if height> 3:
    print("You can able to ride")
    age=int(input("What is your age? "))
    if age<12:
        print("Please pay 150 Rs.")
    elif age<=18:
        print("Please pay 250 Rs.")
    else:
        print("Please pay 500 Rs.")
else:
    print("can't ride")
print("bye")

