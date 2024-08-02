#Arithmetic Operators

print (10 + 3)   #13
print (10 - 3)   #7
print (10 * 3)   #30
print (10 / 3)   #3.33333
print (10 ** 3)  #10 power of 3 => 1000
print (10 // 2)  #Quotient
print (10 % 2)   #Reminder

print(4+4)
print(4-4)
print(4*4)
print(4/4)
print(4**4)
print(4//4)
print(5%2)
print(5+4*3-1+10/5)

a = 5
b = 2
print(a/b)

#Assignment Operators (Loops)

a = 10
print (a)     # 10

a = 5
print (a)     # 5

a += 10       # a = a + 10
print (a)     # a = 15

a *= 2        # a = a * 2
print (a)     # a = 30


a,b = 2,3
c = a + b
a += 5
c += a
print(c)

a,b = 4,3
c = a - b
a -= 5
c -= a
print(c)

a,b = 2,3
c = a * b
a *= 5
c *= a
print(c)

a,b = 3,3
c = a / b
a /= 5
c /= a
print(c)

a,b = 2,3
c = a ** b
a **= 5
c **= a
print(c)

a,b = 10,3
c = a // b
a //= 5
c //= a
print(c)


# Comparision Operators - return T/F
# (If Else, Loops)

print (10 == 10)   # T
print (10 != 10)   # F
print (10 >= 10)   # T
print (10 > 10)    # F
print (10 <= 10)   # T
print (10 < 10)    # F


a = 5
print(a==5)
print(a!=5)
print(a<=5)
print(a>=5)
print(a<5)
print(a>5)
print((a+1) !=6)

#Logical Operator and, or, not
# (If Else, Loops)

print (10==10 and 4<6)       # T and T => T
print (10==10 and 4>6)      # T and F => F
print (10==10 or 4>6)       # T or F => T
print (not 10==10)          #not T => F

a,b = 5,3
print(a<3 and b==3)
print(a<3 or b==3)
print(not(a))

a,b = 4,3
c = False
print(not(c))

a,b = 4,3
c = True
print(a<=4 and c)

a,b = 4,3
c = False
print(a<=4 and c)

a,b = 4,3
c = True
print(a<=4 or c)


#Example Program:
is_magician = True
is_expert = False

if is_expert and is_magician:
    print("You are a Mater Magician")
elif is_magician and not is_expert:
    print("At least you're getting there")
elif not is_magician:
    print("You need Magic Powers")        


#Bitwise operatoers

# &     # and
# |     # or
# ^     # xor
# ~     # not(Compliment)
# <<    # leftshift
# >>    # Rightshift

a,b=5,4
print(a & b)
print (a | b)
print (a ^ b)
print(~a)
print(~b)
print(a << 2)
print(a >> 2)


a,b,c,d,e,f,g= 26,23,17,24,45,68,56

x1 = a & b
print(x1)

x2 = c | d 
print(x2)

x2 = c ^ d 
print(x2)

print(~e)

x3 = f << 2
print(x3)

x4 = g >> 3
print(x4)


#Identity operator

a = 5
b = 5
print (id (a))
print (id (b))
print (a is b)

a = 5
b = 5
print (id (a))
print (id (b))
print (a is not b)

a = 5
b = '5'
print (id (a))
print (id (b))
print (a is b)

a = 5
b = '5'
print (id (a))
print (id (b))
print (a is not b)

a = 5
print(id(a))

a = 6 
print(id(a))

a = 5
b = 5.0
print (id (a))
print (id (b))
print (a is b)

a = 5
a = 8
print (id (a))
print (id (a))
print (a is a)

#Membership Operator 

str = 'Hariharan'
print("Hari" in  str)

str = 'Hariharan'
print("ri" in  str)

str = 'Hariharan'
print("Ha" in  str)

str = 'Hariharan'
print("hari" in  str)

str = 'Hariharan'
print("hari" not in  str)

str = 'Hariharan'
print("V" not in  str)


l1 = [2,7,0,-7,45] 
print(2 in l1)

l1 = [2,7,0,-7,45] 
print(20 in l1)

l1 = [2,7,0,-7,45] 
print(20 not in l1)

l1 = [2,7,0,-7,45] 
print(-7 not in l1)