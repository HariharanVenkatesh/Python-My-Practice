#Global keyword in python
def display():
    a=20
    def show():
        global a
        a=30
    print(f"value of a Before calling show() function is {a}")
    show()
    print (f"value of a after calling show() function is {a}")
display()
print(a)