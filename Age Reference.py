#create a program to show the age gap compared to yours

ma=float(input("Enter age of person wrt whome you want to see that are you older or younger !"))
age=float(input("Enter your age:   "))
gap=ma-age
if(ma>age):
    print("You are younger than him/her , by ",gap," years !")
elif(ma<age):
    gap=gap*(-1)
    print("You are older him/her, by  ",gap," years !")
else:
    print("We both have same age !")
