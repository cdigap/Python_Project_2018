# Ashok Gangadharan 2018-04-13
# Python Project...
# 
# Plotting Graph for the different Iris Setosa flower , Average Sepal & Petal data
#

import matplotlib.pyplot as plt
import csv

# Species Specific arrays
xsl = []
ypl = []
xsw = []
ypw = []

# count for getting the number of records
count = acount = bcount = 0

# Sepal and Petal Data - Versicolor
sl = sw = pl = pw = 0

# Sepal and Petal Data - Setosa
vsl = vsw = vpl = vpw = 0

# Sepal and Petal Data - Virginica
ssl = ssw = spl = spw = 0

# Average Sepal and Petal Data - Versicolor
asl = asw = apl = apw = 0

# Average Sepal and Petal Data - Setosa
avsl = avsw = avpl = avpw = 0

# Average Sepal and Petal Data - Virginica
assl = assw = aspl = aspw = 0

# Over all Average Sepal and Petal Data - All
lent = []
wid = []

def avg(S,C):
    """This Function returns the average of the numbers given"""
    avg = 0
    avg = S/C

# Returns the rounded to 2 decimal places...
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


# Calculating Average and Assigning Sepal and Petal Data into the variables - Versicolor
asl = avg(sl,count)
asw = avg(sw,count)
apl = avg(pl,count)
apw = avg(pw,count)

# Appending Sepal and Petal data into the Over all Lenght and Width Array, lent and wid respectively - Versicolor
lent.append(asl)
lent.append(apl)
wid.append(asw)
wid.append(apw)

# Appending Sepal and Petal data into the Lenght and Width Array, lent and wid respectively - Versicolor
xsl.append(asl)
xsw.append(asw)
ypl.append(apl)
ypw.append(apw)

# Calculating Average and Assigning Sepal and Petal Data into the variables - Setosa
assl = avg(ssl,acount)
assw = avg(ssw,acount)
aspl = avg(spl,acount)
aspw = avg(spw,acount)

# Appending Sepal and Petal data into the Over all Lenght and Width Array, lent and wid respectively - Setosa
lent.append(assl)
lent.append(aspl)
wid.append(assw)
wid.append(aspw)

# Appending Sepal and Petal data into the Lenght and Width Array, lent and wid respectively - Setosa
xsl.append(assl)
xsw.append(assw)
ypl.append(aspl)
ypw.append(aspw)

# Calculating Average and Assigning Sepal and Petal Data into the variables - Virginica
avsl = avg(vsl,bcount)
avsw = avg(vsw,bcount)
avpl = avg(vpl,bcount)
avpw = avg(vpw,bcount)

# Appending Sepal and Petal data into the Over all Lenght and Width Array, lent and wid respectively - Virginica
lent.append(avsl)
lent.append(avpl)
wid.append(avsw)
wid.append(avpw)

# Appending Sepal and Petal data into the Lenght and Width Array, lent and wid respectively - Virginica
xsl.append(avsl)
xsw.append(avsw)
ypl.append(avpl)
ypw.append(avpw)

# calling plt to create a Histogram for the average of all the three type of Iris flowers

plt.hist([lent, wid], bins=6, rwidth=0.80, color=['red','blue'], label=['Sepal & Petal Width','Sepal & Petal Length'])


plt.ylabel('Count')
plt.xlabel('Average Width and Length')
plt.title('Fishers Iris Data\n Summary')
plt.legend()
plt.show()
