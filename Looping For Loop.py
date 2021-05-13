#For loops
#sequence= characters in sequense, e.g l=["p","y","t","h","o","n"]

sequence=["at","the","end","of","the","loop"]
for character in sequence:
    print(character)
#this program works= in first iteration 'at' will be stored in character in second next willbe stored and it goes long as last item



print("==========================================")
print("*******Looping through strings*********")
#looping through strings
s="Aditya Malode"
for character in s:
    print(character)
#works same as lists bu now each character of string will stored in character and willstore next in next itteration




#python count in for statement
print("==========================================")
print("-------Python Range-------")
for count in range(1,15):
    print(count)
    
    

#This following will print multiplication of number given by user to the numbers in range    
print("==========================================")
n=int(input("Enter a number"))
for count in range(1,10):
    p=n*count
    print(p)
    
    
    
    
#here both number and range both are given by user
print("==========================================")
n=int(input("Enter a number"))
r1=int(input("Enter initial range value:  "))
r2=int(input("Enter final range value:  "))
for count in range(r1,r2):
    print(n*count)
    
