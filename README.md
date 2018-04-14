# Python Project 2018 with Fisher's Iris Data Set

The Dataset used is coming from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris). 

The Project entails doing research on the Iris Data and collect background information, writing a Summary of the Data Set. Summarise the dataset by writing Python Scripts.  Need to create Supporting details like Tables, graphics which could easily explain what we are trying to bring forward with visual representation.

The Fisher's Isis Data set is also called Iris Flower Data Set, which helps in understanding the different aims and background ![Ronald Fisher](https://github.com/cdigap/Python_Project_2018/blob/master/Images/R._A._Fischer.jpg) of each of  the different forms of the observations and analysis.  This Data Set was introduced by the British Statistician and biologist Ronald Fisher in 1936. It is sometimes also referred as Anderson's Iris data set as Edgar Anderson collected the data to quantify the form and stucture of the organisms and their specific structural features([Morphology](https://en.wikipedia.org/wiki/Morphology_(biology))).

## Description

The data collected is of 3 species of *iris* flowers, they are Iris setosa, Iris Versicolor and Iris Virginica.

<img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_Setosa.jpg" width="256" height="256" title="Iris setosa"> <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_Versicolor.jpg" width="256" height="256" title="Iris Versicolor"> <img src="https://github.com/cdigap/Python_Project_2018/blob/master/Images/Iris_virginica.jpg" width="256" height="256" title="Iris Virginica">

The measurements of 50 flowers were taken in Centimeters of variables of below mentioned 4 features. 
* Sepal Length 
* Sepal Width
* Petal Lenght 
* Petal Width


## Reference
* https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/ - For Plotting graphs
* https://stackoverflow.com/questions/12236566/setting-different-color-for-each-series-in-scatter-plot-on-matplotlib -  for Different color for different attributes
* https://youtu.be/WbTOutpwPHs Good Videos on how to work with Matplotlip.pyplot
* https://matplotlib.org/2.0.2/api/colors_api.html - Colors

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
