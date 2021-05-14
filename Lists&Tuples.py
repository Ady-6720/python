# program to add name of user at end of the predefined list

l=["John","Keith","Parry","Loki"]
N=str(input("Please enter your name:  "))
l.extend([N])
print("Updated list:   ",l)


#to add an item at end of list    Listmane.EXTEND[index]    is used
#to replace or add an item at specific position listname.append[index] is used

# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete entire list
del my_list

# Error: List not defined
print(my_list)
