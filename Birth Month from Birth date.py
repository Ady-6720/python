#program to print the month in which user is born by taking ddmmyyyy format.
t=["Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
bd=input("Enter your date of birth in DD-MM-YYYY format use dashes properly:  ")
i=int(bd[3:5])-1
bdm=t[i]
print("You were born in ",bdm)

#here we used slicing of string just to get only month index in index variable
