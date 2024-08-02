# Type Casting - Type Casting is Nothing But Changing a One type of Datatype into Another Type of Data Type

a = float (10)
print (a, type (a))

b = int(14729873.69)
print (b, type (b))

c = str (10) # c = "10"
print (c, type (c))

d = int("89")
print (d, type (d))

e = bool (0)
print (e, type (e))

#Typecasting

length = len("Hariharan")
print("Your name has "+str(length)+" Characters")
new_length =str(length)
print(type(new_length))
print(type(length))



print(10+10)

print("10"+"10")

print(int("10")+int("10"))

print(10+float("10"))



name="Hariharan"
print(10 + int(name))


name="2323"
print(10 + int(name))


#Example No 1:
#Without type casting

First_no = input("enter first number: ")
Second_no = input("enter second number: ")

sum = First_no + Second_no
print(sum)

#with typecasting

First_no = input("enter first number: ")
Second_no = input("enter second number: ")

sum = int(First_no) + int(Second_no)
print(sum)


#Example NO 2:
#Without typecasting

number = input("enter a two digits number: ")
first_digit = number [0]
second_digit = number [1]
print (first_digit + second_digit)

#With type casting

number = input("enter a two digits number: ")
first_digit = number [0]
second_digit = number [1]
print (int (first_digit) + int(second_digit))

#Example No 3:
#input () Python Standard Function

print("Enter a Number")
a = input ()
x = int(a)
print("the value of x is", x, type (x) )

print ("Enter a Number")
b = int (input())
print("the value of b is", b, type (b))

c = x + b
print ("the total of c is", c, type (c))

#Example No 4:
#input () Python Standard Function

print ("Enter a Number")
a = input ()
x = float (a)
print("the value of x is", x, type (x) )

print ("Enter a Number")
b= float (input())
print("the value of b is", b, type (b))

c = x + b
print ("the total of c is", c, type (c))

