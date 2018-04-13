# Ashok Gangadharan 2018-04-09
# Python Project...
# 
# Plotting Graph for the different Iris Setosa flower , Average Sepal & Petal data
#

import matplotlib.pyplot as plt
import csv

x = []
y = []
a = []
b = []
count = 0
sl = 0
sw = 0
pl = 0
pw = 0
asl = 0
asw = 0
apl = 0
apw = 0


def avg(S,C):
    """This Function returns the average of the numbers given"""
    avg = 0
    avg = S/C

    return round(avg,2)

with open('iris_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
       if row[4] == "Iris-virginica":
           x.append(float(row[0]))
           y.append(float(row[1]))
           a.append(float(row[2]))
           b.append(float(row[3]))
           count += 1
           sl += float(row[0])
           sw += float(row[1])
           pl += float(row[2])
           pw += float(row[3])
            
asl = avg(sl,count)
asw = avg(sw,count)
apl = avg(pl,count)
apw = avg(pw,count)

# calling plt to create a scatter graph

plt.scatter(asl,asw, marker="o", label='Sepal',color=['red','green'])

plt.scatter(apl,apw, marker="*", label='Petal',color=['yellow','blue'])


plt.ylabel('Length')
plt.xlabel('Width')
plt.title('Fishers Iris Data\n Iris-Virginica')
plt.legend()
plt.show()

