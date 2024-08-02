#range() function in python

a = range(5)
print(a[0])
print(a[1])


a = range(2,5)
print(a[0])


a = range(2,5)
for i in a:
    print(i)


a = range(2,15,2)
for i in a:
    print(i)    


a = range(2,15,3)
for i in a:
    print(i)    


a = range(2,15,-3)   #Acoording to the formula i=2,j=15,k=-3  (i,i+k,i+2k,i+3k.........j-1)
for i in a:
    print(i) 



a = range(2,15,0)            #Value Error  range() arg 3 must not be zero
for i in a:
    print(i)


a = range('2',15,0)            # error:'str' object cannot be interpreted as an integer
for i in a:
    print(i)


a = range(10,0)
for i in a:
    print(i)

a = range(10,0,-1)
for i in a:
    print(i)

    
a = range(-1,-10,-1)
for i in a:
    print(i)


total = 0
for i in range(1,101):
    total += i
print(total)


a = range(1,101)
b = 0
for i in a:
    b = i+b
print(b)
