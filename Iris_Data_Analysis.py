# Ashok Gangadharan 2018-04-15
# Python Project...
# 
# Analysing Data from the file... 
#
import numpy as np
import pandas as pd 

from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt

#Assigning the data File to dfile
dfile = "iris_data.csv"

#Defining Headers to the file
colms = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']

# data File getting the Headers assigned.
data_file = pd.read_csv(dfile,names=colms)

# Details of each columns identified being generated and displayed.
data_file.info()

#Displaying the Number of Lines each type/Species of flower has in the file.
print(data_file.groupby('Species').size())

# Displaying the description of file Like the Cout, Mean, Standard deviation, 
# Minimum and Maximum (length and Width) 
print(data_file.describe())

# Plots box chart with easily readable/understandable the mean, min and max and the outliers of each flower
data_file.plot(kind='box', subplots = True, layout = (1,4), sharex = False, sharey = False, title='Summary Box Plot')

# Plots for individual Dimentions - Sepal, Petal - Length and Breadth
# https://stackoverflow.com/questions/18498690/boxplot-with-pandas-groupby
fig, ax = plt.subplots()

data_file.boxplot(column=['Sepal_Length'], by='Species', ax=ax)

fig, ax = plt.subplots()
data_file.boxplot(column=['Petal_Length'], by='Species', ax=ax)

fig, ax = plt.subplots()
data_file.boxplot(column=['Sepal_Width'], by='Species', ax=ax)

fig, ax = plt.subplots()
data_file.boxplot(column=['Petal_Width'], by='Species', ax=ax)


# Plots a histogram with 15 containers to show the distribution of the flowers dimentions
data_file.hist(bins=15)

#plt.show()
# Plots a Scatter mattrix chart...
scatter_matrix(data_file)

plt.show()
