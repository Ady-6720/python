#program to giveuser what he wants from predefined dictionary using dictionary operations

print("This program will tell you Name,age,gender,address,phone of a person just enter what you want! ")

info={"name":"John Will","age":"22","gender":"Male","address":"12Street, Bakery road, Berkley","phone":"220-432-8794"}
i=str(input("What do you want to know: ")).lower() #lower fuction makes user input in lowercase letters completely
print(info.get(i,"Not found"))

#here we used get function and assigned key variable i to get info
