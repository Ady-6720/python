#matplotlib is used to visualize data in forms of bar, histograph etc
import matplotlib.pyplot as plt     #importing matplotlib
x=[1,2,3,4,5,6,7,8,9,10,11,12]            #this list will be used as data on x axis
y=[10,11,44,9,12,33,48,100,4,27,104,55]    #this willbe data on y axis
plt.plot(x, y)              #this will plot in form of point which are joined with lines
plt.show()

legend=["Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
plt.bar(legend, y)               #this will be a barchart 

plt.show()


plt.hist(x)                 # Function to plot histogram
plt.show()                  # Function to show the plot


plt.scatter(x, y)           # Function to plot scatter
plt.show()                  # function to show the plot