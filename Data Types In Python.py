# Collections
# List - collection of data types

#     0  1  2   3   4 5     6    7  8    9               #indexes
a = [1,2.88,3,False,5,6, "world",8,9.99,10,1,1,1,1,1]    # allows duplicates
print(a, type (a))
print(a[3])                                              # ordered
a[3] = True                                              # modify
print(a)

#Excercise : Check for Duplicates in list using loops (Note:Don't use sets Here)

Random_list = ['a','b','c','b','d','m','n','n'] 

Duplicates = []
for value in Random_list:
    if Random_list.count(value) > 1:
        if value not in Duplicates:
            Duplicates.append(value)

print(Duplicates)

#List Slicing

Amazon_cart = ["Gadgets","Accessories","Cloths","Groceries"]
# print(Amazon_cart[0:]) 
# print(Amazon_cart[0:1:]) 
# print(Amazon_cart[::-1])    #Reverse slicing
Amazon_cart[0] = "Big Billion Days"
New_cart = Amazon_cart[0:]                      #Copying vs MOdifying the list
New_cart [0] = "Big Deals"
print(New_cart)
print(Amazon_cart)

#Nested list in Python [list within a list]
# For ex:[1,45,23,18,[25,27,5,22]7,11,21,8]

list1 = [1,45,23,18,[25,27,5,22],7,11,21,8]
print(len(list1))
print(list1[4][2])
print(list1[len(list1)-5])
print(list1[4][3])
print(list1[4][:])
print(list1[4][0:3])
print(list1[4][0:4])
print(list1[4][::2])
list2 = [10,34,90,['Hariharan','Aswin','Abi','Cali'],89]
print(list2[3][2])


# Tuple collection of data types 

#    0  1   2   3   4 5     6    7  8     9            #indexes
a = (1,2.88,3,False,5,6, "world",8,9.99, 10,1,1,1,1,1) # allows duplicates
print(a, type(a))
print(a[8])                                            # ordered
a[6] =6666                                             # unmodify


tuple1 = (12,6, -8, 'jenny', True, 12,6)
tuple2 = (45,67,90)
tuple3 = tuple1 + tuple2
tuple = (23,)*23
list1 = [1,2,3,5]
tuple1 [0]=13
print(tuple)

# Set

a = {1,1,1,"a","a","a","b","b","c","c"}      # no duplicates, unordered, unindexed
print(a, type(a))


my_set = {1,2,3,4,5}
your_set ={4,5,6,7,8,9,10}

print(my_set.difference(your_set))           #Return the difference of two or more sets as a new set.
print(my_set.discard(5))                     #Remove an element from a set if it is a member.Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.
print(my_set)
print(my_set.difference_update(your_set))    #Remove all elements of another set from this set.
print(my_set)
print(my_set.intersection(your_set))         #Return the intersection of two sets as a new set.
print(my_set.isdisjoint(your_set))
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))
print(my_set.union(your_set))


set1= {10,5 ,56,89,90, 'Rocky', True}
set2=set()
set1.add([13,14,15])    #in set you can add any unchengable items like tuple
set1.pop()              # randomly removes 
set1.remove(56)         #remove 
set1.clear()            #to clear a entire set
set1.discard()          #remove
print(set1)
print (type (set2))



#Sets Methods 
#Operations on sets

set1= {'Hariharan','Aswin','Abi','Caleb'}
set2= {'Hariharan','Aswin','Abi','Pradeep','Dravid','Caleb','Shajith','Sarvesh'}
set3= {'Hariharan','Aswin','Abi','Pradeep','Dravid','Caleb','Shajith','Sarvesh'}
print(set1. union(('Arun', 'Gopi')))
set1.update([ 'Arun', 'Gopi'])
print(set1) 
set1 |= set2
set2.union (set1)

print(set1. intersection(['Arun','Gopi']))
print(set1 & set2 & set3)
set2.intersection_update(['Arun','Gopi'])
print (set1)
print(set2)


set1= {'Hariharan','Aswin','Abi','Caleb','Arun','Gopi'}
set2= {'Hariharan','Aswin','Abi','Pradeep','Dravid','Caleb','Shajith','Sarvesh'}
set3= {'Hariharan','Aswin','Abi','Pradeep','Dravid','Caleb','Shajith','Sarvesh'}
print(set1.difference(set2))
print(set1.difference(('Mani','Viji')))
print(set1.difference(set2,set3))
print(set1 - set2)
set1.difference_update(set2)
print(set1)
print(set2)


set1= {'Hariharan','Aswin','Abi','Caleb','Arun','Gopi'}
set2= {'Hariharan','Aswin','Abi','Pradeep','Dravid','Caleb','Shajith','Sarvesh'}
set3= {'Hariharan','Aswin','Abi','Pradeep','Dravid','Caleb','Shajith','Sarvesh'}
print(set1.symmetric_difference(set2))
print(set1 ^ set2 ^ set3)               #this is also used for a symmetric_differance
set2.symmetric_difference_update(set1)
print(set2)
set1.symmetric_difference_update(('Naveen','Ranjith'))
print(set2)
print(set1)


set1 = {'Hariharan','Aswin','Caleb','Abi'}
set2 = {'Hariharan','Pradeep','Dravid','Dhanush'}
print(set1.isdisjoint(set2))

set1 = {'Hariharan','Aswin','Caleb','Abi'}
set2 = {'Pradeep','Dravid','Dhanush'}
print(set1.isdisjoint(set2))


set1 = {'Hariharan','Aswin','Caleb','Abi'}
set2 = {'Pradeep','Dravid','Dhanush'}
print(set1.isdisjoint(['Prashanth','Dinesh','Hariharan']))
print(set1.issubset(['Prashanth','Dinesh','Hariharan']))
print(set1.issubset(set2))
print(set1 <= set2)
print(set1 <= set1)
print(set1.issuperset(set2))
print(set1 >= set2)
set2.clear()
del set2 
print(set2)

#Dictionary in Python denoted as {} and Key&Value pair
#Ordered Since python 3.7 version,in previous Unordered Unindexed
#Keys should be immutable and values are mutable,No duplicate members allowed
#1st method to create Dictionary

Employee_Id ={
    'Hariharan':63791,
    'Aswin':63792,
    'Abi':63793,
    'Caleb':63794,
    'Dravid':63795,
    'Pradeep':63796,
    'Shajith':63797,
    "Sarvesh":63798,
    #Arun:63799    #NameError: name 'Arun' is not defined
    #'Abi':12345    #This new value will be appear because no Duplicate allowed         
}
print(Employee_Id)
print(Employee_Id['Dravid'])
print(Employee_Id['dravid'])  #KeyError: 'dravid' Because Python is Case sensitive


#2nd Method to create Dictionary
Employee_Id = dict({
    'Hariharan':63791,
    'Aswin':63792,
    'Abi':63793,
    'Caleb':63794,
    'Dravid':63795,
    'Pradeep':63796,
    'Shajith':63797,
    "Sarvesh":63798,
})
print(Employee_Id)


#3rd Method
Employee_Id = dict([('Hariharan',63791),('Aswin',63792),('Abi',63793),('Caleb',63794),('Dravid',63795),('Pradeep',63796),('Shajith',63797),("Sarvesh",63798)])
print(Employee_Id)

Employee_Id ={
    'Hariharan':63791,
    'Aswin':63792,
    'Abi':63793,
    'Caleb':63794,
    'Dravid':63795,
    'Pradeep':63796,
    'Shajith':63797,
    "Sarvesh":63798
}
print(Employee_Id)
Employee_Id['Caleb'] = 73737
print(Employee_Id)

print(Employee_Id)
Employee_Id['Arun'] = 73737
print(Employee_Id)

print(Employee_Id)
Employee_Id['Arun'] = 73737
Employee_Id['Pradeep'] = {'Pradeep_Home':12345,'Pradeep_work':54321}
print(Employee_Id)
print(Employee_Id['Pradeep'])
print(Employee_Id['Pradeep']['Pradeep_work'])
print(Employee_Id.get('Shajith'))
print(Employee_Id.get('shajith'))     # o/p:None 


Data = {
    1:'Hariharan',
    2:'Aswin',
    0:'Caleb'
}
print(Data[0])

print(Employee_Id)
del Employee_Id['Dravid']
print(Employee_Id)

print(Employee_Id)
print(Employee_Id.pop('Sarvesh'))
print(Employee_Id)

print(Employee_Id)
print(Employee_Id.popitem())
print(Employee_Id)

print(Employee_Id)
print(Employee_Id.clear())
print(Employee_Id)

print(Employee_Id)
print(Employee_Id.keys())
print(Employee_Id.values())
print(Employee_Id.items())

for i in Employee_Id:
    print(i)
    print(Employee_Id[i])

for i in Employee_Id.items():
    print(i)
        
print(Employee_Id)
print(Employee_Id)
Employee_Id2 = Employee_Id.copy()
print(Employee_Id) 
print(len(Employee_Id))

#Nested dictionaries&List in Python
#Dictionary within the Dictionary (Multiple Level of Nesting also Possible)
 

Voters_Detail = {
    'Hariharan' : {'Roll_no':1007,'Age':22,'Voting_Place':"Nondimedu"},
    'Aswin': {'Roll_no': 121,'Age':23,'Voting_place':"Kaandhal"}
}
print(Voters_Detail)
print(Voters_Detail["Hariharan"])
print(Voters_Detail["Hariharan"]["Roll_no"])
Voters_Detail["Aswin"]["Phone_no"] = 9876543210
print(Voters_Detail["Aswin"])
del Voters_Detail["Aswin"]["Phone_no"]
Voters_Detail["Aswin"].pop(("Phone_no"))
print(Voters_Detail["Aswin"])

#Nesting a list in dictionary

Travel_data = {
    "Gujarat":["Dwarkadhish","Somnath","Statue of Unity"],
    "Rajasthan":["Jaipur","Udaipur"]
}
print(Travel_data)
print(Travel_data["Rajasthan"])


#Dictionaries Within the list
Voters_Detail = [
    {"Name":"Hariharan",'Roll_no':1007,'Age':22,'Voting_Place':"Nondimedu"},
    {"Name":"Aswin",'Roll_no': 121,'Age':23,'Voting_place':"Kaandhal"}
]
print(Voters_Detail[0])
print(Voters_Detail[1])
print(Voters_Detail[2])   #IndexError: list index out of range



Voters_Detail = [
    {
        "Name":"Hariharan",
        'Roll_no':1007,
        'Age':22,
        'Voting_Place':"Nondimedu"
    },
    {
        "Name":"Aswin",
        'Roll_no': 121,
        'Age':23,
        'Voting_place':"Kaandhal",
        'Phone_no':[63791,98765]
    }
]
print(Voters_Detail)
print(Voters_Detail[1]["Phone_no"])
