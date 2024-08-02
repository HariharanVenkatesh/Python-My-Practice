#local vs global scope in python

a = 10            #Global
def display():
    a = 15        #Local
    print(a)
display()    

a = 10            #Global
def display():
    #a = 15        #Local
    print(a)
display()    

#a = 10            #Global
def display():
    a = 15        #Local
    print(a)
display()    
print(a)

a = 10            #Global
def display():
    a = 15        #Local
    def show():
        print(a)
    show()    
display()    
#print(a)

a = 10            #Global
def display():
    a = 15        #Local
    def show():
        print(a)
#show()    #NameError: name 'show' is not defined
display()    
print(a)