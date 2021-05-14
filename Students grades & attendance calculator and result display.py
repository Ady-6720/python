#This is a program to calculate student grades and student attendance percentage and show them if they are passed or failed if failed why so.
#This program is modified so that errors and crashes will avoided in case of invalid inputs such as strings and other inputs other than float values or int values.

#data validation
#if student enters grades below 0 or above 10 then data will be invalid

data_valid=False
#in this loop if data is less then 0 or greater than 10 is given loop will give o/p as invalid data and continue to take input again till valid data is entered
while data_valid==False:
    grade1=input("Enter your grade of first test: ")
    try:
        grade1=float(grade1)
    except:
        print("Enter a valid Integer !")
        continue
    if(grade1<0 or grade1>10):
        print("Data invalid! Please enter grade value in between 0 to 10, Enter again!")
        continue            #if data is invalid this function will get back control to line 6 again and will continue till valid data is fed
    else:
        data_valid=True
    
data_valid=False    
while data_valid==False:  
    grade2=input("Enter your grade of second test: ")
    try:
        grade2=float(grade2)
    except:
        print("Enter a valid Integer !")
        continue
    if(grade2<0 or grade2>10):
        print("Data invalid! Please enter grade value in between o to 10, Enter again !")
        continue
    else:
        data_valid=True
        
data_valid=False
while data_valid==False:
    total_classes=input("Enter total number of classes:  ")
    try:
       total_classes=float(total_classes)
    except:
        print("Enter a valid Integer !")
        continue
    if total_classes<=0:
        print("Data invalid! Total Classes shoul be greater than 0, Enter again!")
        continue
    else:
        data_valid=True
    
    
data_valid=False
while data_valid==False:    
    absences=input("Enter total no of Absences:  ")
    try:
       absences=float(absences)
    except:
        print("Enter a valid Integer !")
        continue
    if absences<0 or absences>total_classes:
        print("Absenses should be between zero and total number of classes, Enter Again!")
        continue
    else:
        data_valid=True
        


avg_grades=(grade1+grade2)/2
attendance=((total_classes-absences)/total_classes)*100

#printing av grades and attendance

print("Your average grades:",avg_grades)
print("Your attendance percentage is:",attendance,"%")

#Rules: Grades are 0-10
#Student need at least 80% attendance to get approval
#Student with 6 or higher willget approval


             #We will use nested if blocks 
if(avg_grades>=6):
        if(attendance>=80):
            print("The student is approved !")
        else:
            print("The student has failed to complete attendance criteria !")

 #as we have to check wether student is having passing attendance if he failed to achieve the passing grades or not we have used ELIF....Else statement 

elif(attendance>=80):
    print("The student has failed due to less grades than passing !")
else:
    print("The student has failed due to less grades than passing and also failed to complete attendance criteria !")
