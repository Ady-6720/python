#guess game while loop
import random    #we imported random lib as we have to assign random number which is to guess
n= random.randint(0,10) #here random number will be choosen from 0-10
m=float(input("Guess the number: "))
while True:
    if m==n:
        print("You guessed it its ",n)
        break
    else:
        m=float(input("Nope! Guess again:  "))
        
        
#here we dont used a static variable instead random is used so we dont have to change number everytime