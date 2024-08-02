#Print vs Return In Python

def func1(a,b):
    c = a + b
    print(c)
func1(3,4)  

def func1(a,b):
    c = a + b
    return c
output = func1(3,4)
print(output)   


def func1(x):
    return x+1

def func2(a,b):
    c = a + b
    return c
output2 = func2(3,4)
final_output = func1(output2)
print(final_output)    

