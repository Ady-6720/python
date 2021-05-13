#Looping statements

#while loop
people=[]
while len(people)<5: #we can use x as a variable and use x=0 as initial value
    p=input("enter your name: ")
    people.append(p)
    #x += 1  #this is increment function used instead of x=x+1
print(people)


#python count
print("========================================")
print("-------Python Range-------")
count=0
while count<=20:
    print(count)
    count = count+1