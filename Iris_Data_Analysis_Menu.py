# Ashok Gangadharan 2018-04-20
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

# Defining a Menu function
def menu():
    print('1. View Info')
    print('2. View Summary')
    print('3. View Full Data')
    print('4. Plot Box Chart')
    print('5. Plot Histogram')
    print('6. Plot Scatter Matrix')
    print('7. Exit')


    
while True:
    menu()
    try:
        user_input = int(input("Enter a Number : "))
        if user_input == 1:
            print(data_file.info())
        elif user_input == 2:
            print(data_file.describe())
        elif user_input == 3:
            print(data_file)
        elif user_input == 4:
            data_file.plot(kind='box', subplots = True, layout = (1,4), sharex = False, sharey = False)
            plt.show()
        elif user_input == 5:
            data_file.hist(bins=15)
            plt.show()
        elif user_input == 6:
            scatter_matrix(data_file)
            plt.show()
        elif user_input == 7:
            print('Thank you for using the Project - I hope this was helpfull....')
            break
        else :
            print('Invalid Option Selected... Please Select from 1 to 8...')
    except:
        print('Exception...Invalid Selection... Please Select from 1 to 8...')
