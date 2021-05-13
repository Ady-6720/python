#Program to calculate area of circle using Importing math library
print("Program to calculate Area & Circumference of circle")
import math
R=float(input("Enter the value of radius of circle =  "))
A= math.pi * (R**2)
C= 2 * math.pi * R
print("Area & Circumference =  ",round(A,2),round(C,2))

