#AND & OR operators

#program to calculate grades of student
grade1=float(input("Enter your grade of first test: "))
grade2=float(input("Enter your grade of second test: "))
absences=int(input("Enter total no of Absences:  "))
total_classes=int(input("Enter total number of classes:  "))

avg_grades=(grade1+grade2)/2
attendance=((total_classes-absences)/total_classes)*100

#printing av grades and attendance

print("Your average grades:",avg_grades)
print("Your attendamce percentage is:",attendance,"%")

#Rules: Grades are 0-10
#Student need at least 80% attendance to get approval
#Student with 6 or higher willget approval


             #We will use nested if blocks 
if(avg_grades>=6 and attendance>=80):           #if both condition satisfies then will proceed
       print("The student is approved !")
elif(avg_grades<6 and attendance<80): 
     print("The student has failed due to less grades than passing and also failed to complete attendance criteria !")      
elif(attendance<80):
    print("The student has failed to complete attendance criteria !")
elif(avg_grades<6):
     print("The student has failed to complete grades criteria !")

 