#Install all required packages

import pandas as pd 
import matplotlib.pyplot as plt 

#Input data

path = r'C:paste the path here\Example file CV.txt' #data file location, copy the path from your device and paste 

data = pd.read_csv(path, sep='\t') #here we use pandas function to open the data file 

print(data.head())

#Data manipulation 

data['time, min'] = data['time/s']/60 #convert sec to hours
print(data.head())

#Data vizualization, making a CV graph 

fig, ax = plt.subplots()
ax.plot(data['Ecell/V'],data['<I>/mA']) #provide x and y arguments
ax.set(xlabel='Voltage, V', ylabel = 'Current, mA') #label the axes
plt.show()

