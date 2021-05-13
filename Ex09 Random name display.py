#program that asks user to enter 8 names and add them to list, pick a random and print
import random
#while loop
people=[]
while len(people)<8: #we can use x as a variable and use x=0 as initial value
    p=input("enter your name: ")
    people.append(p)
    
index= random.randint(0, 8)
print(people[index])




