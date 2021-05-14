#program to showuser his typing elapses and mistakes and plot a graph from data
#first install matplotlib, by going to cmd prompt as admin and give command = pip install matplotlib
#also if you are using spyder then go to options in console section and unmark mute inline
#if still you are unable to see the plots comment or send a mail or messege me on LinkedIN

import time as t
import matplotlib.pyplot as plt
import random


time=[]
mistakes=0

#in this block we will randomize the word which is to be used for typing test
words=["programming","shoeless","opticfiber","xylophone","thunderstorm","handkerchief"]
w=random.randint(0,len(words)-1)
f=str(words[w])

print("This program will show you how much time you taken to type   ",str(f),"    word, and also will show how much you progressed.")
input("press ENTER to continue !")
while len(time)<5:              #this loop will run 5 times
    start=t.time()              #this will store start time wrt to apack
    inp=input("Type the word:") #here user will give his inpu by typing the word
    end=t.time()    #here end time will stored wrt apack
    elapsed=end-start #here time taken to type the word will store by doing subtraction operation
    
    time.append(elapsed) #the elapsed time will be stored in time list
    
    if(inp.lower() != str(f)):  #here user input will be cheked if the entered word has mistake then below codeblock will run
        mistakes=mistakes+1
    
print("you made",mistakes," mistakes")
print("Lets see your evolution !")
t.sleep(5)      #further code will be hold till sleep time is over.
x=[1,2,3,4,5]
y=time
plt.plot(x,y)
legend=["1","2","3","4","5"]    #string is used because we want to avoid plots like 1.5,2.5 etc.
plt.xticks(x,legend)            #here legend is used to avoid getting decimal plots on x-axis
plt.xlabel("Time")              #xticks is used to avoid inbetween plots
plt.ylabel("Attempts")          #this is for labelof y-axix
plt.title("Your Typing Evolution!") #this is label for x-axis
plt.show()
