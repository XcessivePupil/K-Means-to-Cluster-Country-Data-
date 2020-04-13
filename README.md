# K-Means-to-Cluster-Country-Data-


This project makes use of unsupervised machine learning in the form of K-Means, clustering of data. 

The program reads in data from one of three datasets. The data included in each set contains the average life expectency and average birth rate for a list of about 200 countries, for the years 1953, 2008 and a combined list of both years.

Following this, the user is asked to input their required number of clusters as well as the number of iterations they wish the program to complete.

The program then creates the requested number of centroids as random datapoints. Using the K-means algorithm each exsisting datapoint is asigned to the nearest centroid. From there the following 2 steps are repeated until either the requested number of iterations are completed or convergence is reached. The mentioned 2 steps:

○ Assign each datapoint to the nearest cluster

○ Compute the means for each cluster as the mean for all the points that belong to it

Comverence in this case is defined as the point at which the means of each cluster reach a
certain "minimum" value and continuing to run the algorithm doesn’t make this value change. 
