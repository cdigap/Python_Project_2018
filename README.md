# Python Project 2018 with Fisher's Iris Data Set

The Dataset used is coming from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris). 

The Project entails doing research on the Iris Data and collect background information, writing a Summary of the Data Set. Summarise the dataset by writing Python Scripts.  Need to create Supporting details like Tables, graphics which could easily explain what we are trying to bring forward with visual representation.

The Fisher's Iris Data set is also called Iris Flower Data Set, which helps in understanding the different aims and background ![Ronald Fisher](https://github.com/cdigap/Python_Project_2018/blob/master/Images/R._A._Fischer.jpg) of each of  the different forms of the observations and analysis.  This Data Set was introduced by the British Statistician and biologist Ronald Fisher in 1936. It is sometimes also referred as Anderson's Iris data set as Edgar Anderson collected the data to quantify the form and structure of the organisms and their specific structural features([Morphology](https://en.wikipedia.org/wiki/Morphology_(biology))).

## Description

The data collected is of 3 species of *iris* flowers, they are Iris setosa, Iris Versicolor and Iris Virginica.

<img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_Setosa.jpg" width="256" height="256" title="Iris setosa"> <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_Versicolor.jpg" width="256" height="256" title="Iris Versicolor"> <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_virginica.jpg" width="256" height="256" title="Iris Virginica">

The measurements of 50 flowers were taken in Centimeters of variables of below mentioned 4 features. 
* Sepal Length 
* Sepal Width
* Petal Length 
* Petal Width

## A High Level Plan

* Week Starting 22nd-April - Write Summary for the project and complete the submission.
* Week Starting 15th-April - Research of better way of plotting the flags and write the scripts accordingly.
* Week Starting 8th-April - Write the initial Scripts for Analyzing Data of Dimensions.
* Week Starting 1st-April - Continue Research and starting writing initial Scripts with Python.
* Week Starting 24/25-March - Research on the Fisher Iris Data set and initiate the project in GitHub.


## Process:
  1.	Research :  on the iris data and understand how to do Data Analysis.
  2.	Load iris data directly with Python.
  3.	Analysis the data.
  4.	Visual Representation of Data.


### Research :
* What is Data Analysis ?
  Data analytics is the pursuit of extracting meaning from raw data using specialized computer systems. These systems transform, 
  organize, and model the data to draw conclusions and identify patterns.
  
  By the definition it can be simple to a very complex algorithm that have developed for different data handling Challenges.
  So for me to the project was to do data Analytics using Python and see what are the different types of patterns / differences or 
  unique features does the iris data set contribute.

*	Load iris data directly with Python.
    
    a.	During initial analysis I found that we can use the csv library to import the txt file and as we know the delimiter used the csv library and imported the matplotlib.pyplot library to plot some graphs.
       
        i. Import csv
        ii. Import matplotlib.pyplot as plt
          
            Opening file 
            with open('iris_data.csv','r') as csvfile:

            Then Start analysing the data. I wrote the a few scripts below – 


## Python Scripts 
* Fisher_Iris_Sepal_Plot.py -  is a Script that will Open the iris_data.csv file using the **csv** library and will read the Sepal length and Sepal Width of the different Iris Flowers and create a Scatter graph to explain how each of the flowers differ. 
  <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_Sepal.png" width="256" height="256" title="Iris Sepal Graph">
* Fisher_Iris_Petal_Plot.py -  is a Script that will Open the iris_data.csv file using the **csv** library and will read the Petal length and Petal Width of the different Iris Flowers and create a Scatter graph to explain how each of the flowers differ.
  <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_Petal.png" width="256" height="256" title="Iris Petal Graph">
* Calculating the Average of the Sepal and Petal data for different flowers and plotting a graph accordingly.
  * Iris_setosa.py - The Script calculates the average of sepal and petal data and plots a scatter graph.
    <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_Setosa.png" width="256" height="256" title="Iris Petal Graph">

  * Iris_versicolor.py - The Script calculates the average of sepal and petal data and plots a scatter graph. 
    <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_versicolor.png" width="256" height="256" title="Iris Petal Graph"> 
    
  * Iris_virginica.py - The Script calculates the average of sepal and petal data and plots a scatter graph.
    <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_virginica.png" width="256" height="256" title="Iris Petal Graph">

  * Iris_Summary_Sct.py - The script that calculates the average of Sepal and petal data and plots an overall Scatter graph for all the 3 different types of Iris flowers.
 
    <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_Summary_Sct.png" width="256" height="256" title="Iris Petal Graph">

* Histogram Graphs to show sets of Data per Flower and a summary.
  * Iris_Summary_Hist.py - The script that calculates the average of Sepal and petal data and plots an overall Histogram for all the 3 different types of Iris flowers.
     
     <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_Summary_Hist.png" width="256" height="256" title="Iris Petal Graph">
     
#### After doing some more research as per my plan I found out that we could do most of the analysis by using the pandas and numpy library. So created the below script using the libraries and built in functionality.

### Iris_Data_Analysis.py 
* This Script generates analytical information for the given Iris_data.csv file. The Script will generate a Data Frame with the details of each columns identified. The scripts generates different graphs to show the distribution of the dimensions.

#### Below is an explanation of what the script does.
*Assigning the data File to dfile*
*Defining Headers to the file*
colms = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']

*data File getting the Headers assigned.*

*data_file = pd.read_csv(dfile,names=colms)*

*Details of each columns identified being generated and displayed.*
data_file.info()


*Displaying the description of file Like the Cout, Mean, Standard deviation,* 
*Minimum and Maximum (length and Width)*
print(data_file.describe())*

*Plots box chart with easily readable/understandable the mean, min and max and the outliers of each flower*
data_file.plot(kind='box', subplots = True, layout = (1,4), sharex = False, sharey = False, title='Summary Box Plot')

*Plots for individual Dimentions - Sepal, Petal - Length and Breadth
https://stackoverflow.com/questions/18498690/boxplot-with-pandas-groupby*
fig, ax = plt.subplots()

data_file.boxplot(column=['Sepal_Length'], by='Species', ax=ax)

fig, ax = plt.subplots()
data_file.boxplot(column=['Petal_Length'], by='Species', ax=ax)

fig, ax = plt.subplots()
data_file.boxplot(column=['Sepal_Width'], by='Species', ax=ax)

fig, ax = plt.subplots()
data_file.boxplot(column=['Petal_Width'], by='Species', ax=ax)

*Plots a histogram with 15 containers to show the distribution of the flowers dimentions*
data_file.hist(bins=15)

*plt.show()
Plots a Scatter mattrix chart...*
scatter_matrix(data_file)

plt.show()

### *Results or output of the scripts in details with the commands explained below.*
#### Details of each columns identified being generated and displayed.
data_file.info() 

  <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/info_1.png"  title="File Info">


##### Displaying the Number of Lines each type/Species of flower has in the file.
print(data_file.groupby('Species').size())
  
  <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/groupby.png"  title="Group By Species">
  

#### Displaying the description of file Like the Cout, Mean, Standard deviation, 
#### Minimum and Maximum (length and Width) 
print(data_file.describe())

  <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/describe.png"  title="Details of the data">

  
### Iris_Data_Analysis_Menu.py
* This script helps the user by menu to easily handle what the user wants to see. The menu is as follows.

  <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Menu.png"  title="Menu">



## Reference
* https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/ - For Plotting graphs
* https://stackoverflow.com/questions/12236566/setting-different-color-for-each-series-in-scatter-plot-on-matplotlib -  for Different color for different attributes (Stackover low has been extremely help ful in a lot of different ways.
* https://youtu.be/WbTOutpwPHs Good Videos on how to work with Matplotlip.pyplot
* https://matplotlib.org/2.0.2/api/colors_api.html - Colors
* https://help.github.com/articles/basic-writing-and-formatting-syntax/#styling-text - Formatting Readme
* https://gist.github.com/uupaa/f77d2bcf4dc7a294d109 - Image resizing for Readme
