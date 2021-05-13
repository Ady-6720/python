#BMI calculator and Category showing
w=float(input("Enter your Weightin Kg:  "))
h=float(input("Enter your Height in meter:  "))
print("You entered",w,"as your weight &",h,"as your height.")

#bmi calculation
#formula BMI=w/(h*h)

bmi=(w/(h*h))
print("Your BMI is :  ",round(bmi,2))

#bmi category determination
#BMI Categories:
#Underweight = <18.5
#Normal weight = 18.5–24.9
#Overweight = 25–29.9
#Obesity = BMI of 30 or greater
if(bmi<=18.5):
    print("You are Underweight !")
elif(bmi>=18.5 and bmi<=24.9):
    print("You are having NORMAL WEIGHT !")
elif(bmi>=25 and bmi<=29.9):
    print("You are OVERWEIGHT !")
elif(bmi>=30):
    print("You are having OBESITY ! ")
else:
    print("Enter valid data!!!!!!!")
    
    
    
    

