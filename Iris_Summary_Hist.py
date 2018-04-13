# Ashok Gangadharan 2018-04-13
# Python Project...
# 
# Plotting Histogram for the different Iris Setosa flower , Average Sepal & Petal data
#

import matplotlib.pyplot as plt
import csv

x = []
y = []
a = []
b = []
count = acount = bcount = 0
sl = sw = pl = pw = 0
vsl = vsw = vpl = vpw = 0
ssl = ssw = spl = spw = 0

asl = asw = apl = apw = 0
avsl = avsw = avpl = avpw = 0
assl = assw = aspl = aspw = 0

lent = []
wid = []

def avg(S,C):
    """This Function returns the average of the numbers given"""
    avg = 0
    avg = S/C

    return round(avg,2)

with open('iris_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
       if row[4] == "Iris-versicolor":
           count += 1
           sl += float(row[0])
           sw += float(row[1])
           pl += float(row[2])
           pw += float(row[3])
       if row[4] == "Iris-setosa":
           acount += 1
           ssl += float(row[0])
           ssw += float(row[1])
           spl += float(row[2])
           spw += float(row[3])
       if row[4] == "Iris-virginica":
           bcount += 1
           vsl += float(row[0])
           vsw += float(row[1])
           vpl += float(row[2])
           vpw += float(row[3])  

# print('after Loop : ')

asl = avg(sl,count)
asw = avg(sw,count)
apl = avg(pl,count)
apw = avg(pw,count)

lent.append(asl)
lent.append(apl)
wid.append(asw)
wid.append(apw)

assl = avg(ssl,acount)
assw = avg(ssw,acount)
aspl = avg(spl,acount)
aspw = avg(spw,acount)

lent.append(assl)
lent.append(aspl)
wid.append(assw)
wid.append(aspw)

avsl = avg(vsl,bcount)
avsw = avg(vsw,bcount)
avpl = avg(vpl,bcount)
avpw = avg(vpw,bcount)

lent.append(avsl)
lent.append(avpl)
wid.append(avsw)
wid.append(avpw)

# calling plt to create a Histogram for the average of all the three type of Iris flowers

plt.hist([lent, wid], bins=6, rwidth=0.80, color=['red','blue'], label=['Sepal & Petal Width','Sepal & Petal Length'])

plt.ylabel('Count')
plt.xlabel('Average Width and Length')
plt.title('Fishers Iris Data\n Summary')
plt.legend()
plt.show()
