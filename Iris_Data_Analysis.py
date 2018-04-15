# Ashok Gangadharan 2018-04-15
# Python Project...
# 
# Analysing Data from the file... 
#
import numpy as np
import pandas as pd 

from pandas.tools.plotting import scatter_matrix

import matplotlib.pyplot as plt

dfile = "iris_data.csv"
colms = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
# data

data_file = pd.read_csv(dfile,names=colms)

#num_columns = len(data_file.columns)
#num_rows = data_file[0].count()

#msl = data_file[0].mean()
#msw = data_file[1].mean()
#mpl = data_file[2].mean()
#mpw = data_file[3].mean()

print(data_file.groupby('Species').size())
print(data_file.describe())

data_file.plot(kind='box', subplots = True, layout = (2,2), sharex = False, sharey = False)

plt.show()

data_file.hist()

plt.show()

scatter_matrix(data_file)

# data_file.info()

plt.show()
