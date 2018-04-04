# Ashok Gangadharan 2018-03-31
# Python Project...
# 
# Plotting Graph for the 3 different Iris flowers , Petal length, Petal Width
#
import matplotlib.pyplot as plt
import csv

x = []
y = []
a = []
b = []
c = []
d = []


with open('iris_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
       if row[4] == "Iris-setosa":
           x.append(float(row[3]))
           y.append(float(row[2]))
       if row[4] == "Iris-versicolor":
           a.append(float(row[3]))
           b.append(float(row[2]))
       if row[4] == "Iris-virginica":
           c.append(float(row[3]))
           d.append(float(row[2]))

plt.scatter(x,y, marker="*",label='Iris-setosa Details',color=['red','yellow'])
plt.ylabel('Petal Length')
plt.xlabel('Petal Width')
plt.title('Fishers Iris Data')
plt.legend()


plt.scatter(a,b, marker="<", label='Iris-versicolor',color=['blue','orange'])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
#-- plt.title('Fishers Iris-versicolor')
plt.legend()


plt.scatter(c,d, marker="s", label='Iris-virginica',color=['green','brown'])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
#-- plt.title('Fishers Iris-virginica')
plt.legend()


plt.show()


