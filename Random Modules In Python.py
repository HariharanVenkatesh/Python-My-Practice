#Random module
#randint
#randrange
#random()
#uniform()
#choice()
#suffle()

import random
a = random.randint(1,7)
print(a)

a = random.randrange(1,3)
print(a)

a = random.random()
print(a)

a = random.uniform(1,3)
print(a)

l= [2,5,90,-5,89,12,56]
a = random.choice(l)
print(a)

l= [2,5,90,-5,89,12,56]
random.shuffle(l)
print(l)