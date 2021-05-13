#Guess the colour
import random
colour=["red","green","blue","yellow","black","white","orange","pink","brown","purple","voilet"]


while True:
    c=colour[random.randint(0,len(colour)-1)] #we put this here because we want to repeat this code to get random colour each time
    p=input("Guess the colour:  ")
    
    while True:
        if(c==p.lower()): #if condition is true then it will jump to line 14.
            break
        else:     #if condition becomes false the code will run below code block.
            p=input("Nope ! Try again:  ")
    print("Yeahh! You guessed it, it was",c)
    
#here below code will ask user to play it again or not if no then code will break    
    plag=input("Do you want to play again yes/no?")
    if(plag.lower()=='no'):
        break