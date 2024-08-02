#loops
#while loop - numbers
#syntax
"""
while <condition T/F>:
"""


#Normal while loop

a = 1                          #Initialization/Start
while a<=100:                  #condition/End                 
    print(a)
    a += 1                     #Incrementation/Jump
print("loop over")    
#Infinite loop

a = -50                         #Initialization/Start
while a<=100:                   #condition/End
    print(a)
    a -= 1                      #Incrementation/Jump                     #Incrementation/Jump
print("loop over")   

#Ex 1:
sum = 1
while sum <= 5:
    print(sum)
    sum += 1
else:
    print("In else block")
print("out from loop")

#Ex 2:
sum = 1
while sum <= 5:
    print(sum)
    sum += 1
    if sum == 3:
        break
else:
    print("In else block")
print("out from loop")

#Ex 3:
sum = 1
while sum < 1:
    print(sum)
    sum += 1
else:
    print("In else block")
print("out from loop")

#Ex 4:
sum = 1
while sum <= 5:
    print(sum)
    sum += 1
print("Out From loop")    

#Ex 5:
sum = 1
while sum > 0:
    print(sum)
    sum -= 1
print("Out From loop")    

#Ex 6:
sum = 1
while sum < 0:
    print(sum)
    sum -= 1
print("Out From loop")    

#Ex 7:
sum = 5
while sum > 0:
    print(sum)
    sum -= 1
print("Out From loop")    

#Ex 8:
sum = 5
while sum <= 0: print(sum) ; sum += 1
print("Out From loop")    

#Ex 9:
sum = 1
while sum > 0:
    print(sum)
    sum -= 1
else:
    print("in else block")
print("Out From loop")    

#Ex 10:
sum = 5
while sum > 0:
    print(sum)
    sum -= 1
else:
    print("in else block")
print("Out From loop")    

#Ex 11:
sum = 1
while sum <= 5:
    print(sum)
    sum += 1
else:
    print("in else block")
print("Out From loop")   

#Ex 12:
sum = 5
while sum > 0:
    print(sum)
    sum -= 1
    if sum == 3:
        break
else:
    print("in else block")
print("Out From loop")   

#Ex 13:
number = int(input("enter a number(-1 to quit)"))
while number != -1:
    print(number)
    number = int(input("enter a number(-1 to quit)"))
else:
    print("in else block")
print("out from loop")    

#Ex 14:
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break
else:
    print("in else block")
print("out from loop")

#Ex 15:
total = 0
number = int(input("enter a number(0 to quit): "))
while number != 0:
    total = total + number
    number = int(input("enter a number(0 to quit): "))
print("total is",total)



# for loop - str/list/tupleset/dict
# syntax
"""
for <variable> in <str/list/tupleset/dict>:
"""    

# for with string

for x in "Hello World":
    print(x)

     
# for with list

for x in [1,2.23,"Hi im Hariharan",True,66.66]:
    print(x)

#For Loop In Python
#Example No 1:
names = ['Hari','Ash','Cali','Abi']
for i in names:
    print(i)
    if i == 'Ash':
        print("Hey, It's me")

#Example No 2:
numbers = [23,8,11,7,18,22]
squares = []
for i in numbers:
    square = i ** 2
    squares.append(square)
print(squares)