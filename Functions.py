#Functions in python
#general syntax
def greet(name):                        #the code inside this wil not executed till the function is triggerred or called
    print("Hello ",name,",how are you!")  

#program to calculate grades of student depending upon his pattern
def pat2015(a,b,c):
    #in 2015 pattern if percentage is equal to or greater than 40 then student will pass
    r=((a+b+c)/300)*100
    if(r>=40):
        return r
    else:
         print("Failed!")
        
def pat2019(a,b,c):
    r=((a+b+c)/300)*100
    if(r>=35):
          return r                      #return function will assign the value to the r variable and control will moved to r
    else:
         print("Failed!")
        
#let's call the function
name=str(input("Enter your name please:  "))
greet(name)                                 #this is call to function now the code inside defination will get executed since we triggerred the function

#to ask marks obtained in three subjects
a=input("Enter marks obtained in A: ")
    
b=float(input("Enter marks obtained in B: "))
c=float(input("Enter marks obtained in C: ")) 
pat=input("Enter your pattern 2015/2019:  ")
if pat==2015:               #here if pattern enterd is 2015 it will call pat2015 function
    r=pat2015(a,b,c)
    print("Passed with: ",round(r,2),"%")
else:                       #else it will call pat2019 function
    pat2019(a,b,c)
    print("Passed with: ",round(r,2),"%")