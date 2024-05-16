#Install all required packages

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

#Input data

path = r'C:\Users\redam\OneDrive\Desktop\Python with Reda\Raw data\Example file CV.txt' #data file location 

data = pd.read_csv(path, sep='\t') #here we use a function to open the data file 

print(data.head())

#Data manipulation 

data['time, min'] = data['time/s']/60 #convert sec to hours
print(data.head())

#Data vizualization and saving the plot

fig, ax = plt.subplots()
ax.plot(data['Ecell/V'],data['<I>/mA']) #provide x and y arguments
ax.set(xlabel='Voltage, V', ylabel = 'Current, mA') #label the axes
plt.show()

