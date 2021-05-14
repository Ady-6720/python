#This program will help you to choose a person for various games 
#step1: Enter no of people from which you want to choose from
#step2: Enter everyones name one by one press enter after every name
#step3: Wait for 5sec
#step4: Tada you have a name choosen from all names.
# Enjoyyyy!!!!!!!!!!!!!!!!
import random
import time as t
#while loop
people=[]
number_names=float(input("Enter no of people from ehich you want to choose one :"))
while float(len(people))<float(number_names): #we can use x as a variable and use x=0 as initial value
    p=input("Enter name of everyone : ")
    people.append(p)
    
index= random.randint(0, 8)
print("Are you ready !")
t.sleep(5)
print("You have been choosen : ",people[index],"  !!!")
