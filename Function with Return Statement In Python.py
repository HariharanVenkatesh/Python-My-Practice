#Function with Return Statement in python 
#Function with Return Value

def add(a,b):
    c = a + b
    return c
print(add(100,300))
   
def add(a,b):
    return a + b
print(add(100,300))    
   
def add(a,b):
    return a + b
result = add(100,300)
print(result)    
   
def add(a,b):
    c = a + b
    return
result = add(100,300)
print(result)    

def add(a,b):
    c = a + b
result = add(100,300)
print(result)    

def add(a,b):
    c = a + b
    return                       #SyntaxError: 'return' outside function
result = add(100,300)
print(result)    


def format_name(f_name,l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_name = format_name("hari","HARAN")
print(formatted_name)


#Return Multiple values from a Function

import statistics
def mean_median_mode(list1):
    return[statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]
result=mean_median_mode([3,5,45,3,2,1,89])
print(result)

import statistics
def mean_median_mode(list1):
    return[statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]   #A sigle return function can return multiple value
a,b,c = mean_median_mode([3,5,45,3,2,1,89])
print(f"Mean is {a}\nMedian is {b}\nMode is {c}")


import statistics
def mean_median_mode(list1):
    return[statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]   #A sigle return function can return multiple value
    print("End of Function")
a,b,c = mean_median_mode([3,5,45,3,2,1,89])
print(f"Mean is {a}\nMedian is {b}\nMode is {c}")


def add(a,b):
    if a == 0 & b == 0:
        return "You have Entered Zero for Both Variables."
    else:
        return a + b

var1 = int(input("Enter First Variable:\n"))    
var2 = int(input("Enter Second Variable:\n"))  
result = add(var1,var2) 
print(result)
