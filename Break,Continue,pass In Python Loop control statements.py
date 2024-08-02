#Break,Continue,pass in python Loop control statements
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        break
    print("Hi")
print("Out from Loop")       



#Break used only in for and while loop
list1 = ["Hey","Hello","Welcome"]
names = ["Hariharan","Aswin","Abi","Caleb","Pradeep","Dravid"]
for item in list1:
    for name in names:
        print(item,name)
        if item == "Hello" and name == "Abi":
            break
    print("Out from inner loop")
print("Out from outer loop")

    
#Continue 

count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        continue
    print("Hi")
print("Out from Loop")  


for i in range(1,11):
    if i == 3:
        continue
    else:
        print(i)


#Pass - Pass means do nothing its like a none operation

for i in range(1,11):
    pass                         #if you dont have a valid condition or Empty loop

count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        pass
    print("Hi")
print("Out from Loop")  

def fun1():
    pass

