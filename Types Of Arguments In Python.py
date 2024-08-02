#Types of arguments
    #Default
    #Positional
    #Keyword
    #Arbitrary/Variable length
        #Arbitrary positional Argument - arg
        #Arbitrary Keyword Argument - Kwarg

# Positional arguement

def demo(name,dept):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
demo("Hariharan","ECE")

def demo(name,dept):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")  #its gives a meaningless output because in the place of name we gave ECE & the place of dept we gave Hariharan
demo("ECE","Hariharan")

#Keyword arguement
def demo(name,dept):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
demo(name = "Hariharan",dept = "ECE")

def demo(name,dept):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
demo(dept = "ECE",name = "Hariharan")

#Using Both Positional&Keyword Arguement

def demo(name,dept):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
demo("Hariharan",dept = "ECE")

def demo(name,dept):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
#demo(dept = "ECE","Hariharan")                 #It gives syntax error cause positional argument follows keyword argument


def demo(name,subject,dept = "ECE"):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
    print(f"Do you teach {subject} ?")
demo("Hariharan","Python")

def demo(name,subject,dept = "ECE"):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
    print(f"Do you teach {subject} ?")
demo("Hariharan","Python","CSE")                # here we provide a parameter for dept so instead of ECE program use CSE

def demo(name,subject,dept = "ECE"):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
    print(f"Do you teach {subject} ?")         #TypeError: demo() missing 1 required positional argument: 'subject'
demo("Hariharan")  

def demo(name,subject = "Python",dept):        #SyntaxError: parameter without a default follows parameter with a default
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
    print(f"Do you teach {subject} ?")
demo("Hariharan","ECE")


def demo(name,dept,subject = "python"):
    print(f"Hey {name}")
    print(f"Are you from {dept} Department?")
    print(f"Do you teach {subject} ?")
demo("Hariharan","ECE")


#Arbitrary arguments

def add(*numbers):                # single * is used for Arbitrary positional Argument 
    a = 0
    for j in numbers:
        a = a + j
    print(f"sum is {a}")   
add(11,22,33)  
add(-1,10)
add(-10,9)


#Arbitrary positional Argument (*args) & Arbitrary Keyword Argument (**kwargs)

def add(*numbers):                # single * is used for Arbitrary positional Argument 
    a = 0
    for j in numbers:
        a = a + j
    print(f"sum is {a}")   
add(11,22,33)  
add(-1,10)
add(-10,9,11,44,67,87,45)



def person_info(**keyargs):
    for i,j in keyargs.items():
        print(i,j)
person_info(Name = "Hariharan",Age = "22",Dept = "ECE")
person_info(Name = "Aswin",Dept = "ECE")



def person_info(*args,**keyargs):
    for i,j in keyargs.items():
        print(i,j)
    print(args)
person_info(2,3,Name = "Hariharan",Age = "22",Dept = "ECE")
person_info(4,5,6,Name = "Aswin",Dept = "ECE")



def Multiply(*Args):
    a = 1
    for j in Args:
        a *= j
    print(f"The Multiplication of the given number is : {a}")    
Multiply(2,3,-6,8)
Multiply(2,5,8,9,0,6)

