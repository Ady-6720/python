myBoolean= True #dont use quotes, if used it will act as astring
type(myBoolean)

num1=float(input("Enter a number:  "))
num2=float(input("Enter second number:  "))
print(num1>num2)      #here as condition satisfies it will write TRUE
print(num2>num1)      #here as condition doesnt satisfies it will give FALSE as an output
print(num1==num2)
print(num1 != num2)

if (num1 > num2):
    print(num1,"is greater than",num2)
elif(num2>num1):
    print(num2,"is greater than",num1) #if this isnt true the control will go to else statement
else:
    print(num1,"is greater than",num2)

#conditional statements ends with colon unlike C