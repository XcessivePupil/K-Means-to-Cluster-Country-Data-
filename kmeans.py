'''
#K-Means clustering implementation

In summary this file reads in data from a CSV file before using the K-means method to cluster it, according to the user's requirements.

Once the data has been clustered as per the users requirements, the results are printed and some details provided.

Numbered breakdown: 

1. Importing the required modules and defining the functions to be used 
2. Initialisation procedure (reading in and gathering the required data)
3. Implement the K-means algorithm, using appropriate looping (applying the data to our functions and looping through them to completion) 
4. Printing and presenting the results 
 
'''

#====
# 1. Importing the required modules and defining the functions to be used 

import csv # for reading in the csv 
from math import sqrt # for the distance calculation 
import random # for randomisation of the centroids 

# Function that reads data in from the csv files and adds each column to a list 

def readCSV(file):
	with open(file) as csvFile:
	 reader = csv.reader(csvFile, delimiter=',')
	 next(reader) # This skips the top row of the data in order to avoid the headings 
	 csvList = [[row[0], 
	 [float(row[1]),
	 float(row[2])]] for row in reader] #concatenating the 2nd and third columns into floats and storing in a list   
	 csvFile.close()

	return csvList	

# This function computes the distance between two data points

def calcDist(p1, p2):
	return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) #using sqrt imported from Math

# This function calculates the average distance of each point (to be used to calculate new centroids) 

def avDistance(dataPoints):
	z = list(zip(*dataPoints)) #unzip the datapoints in order to add the them to a list and perform calculations 
	birthRate = sum(z[0])/len(dataPoints)
	lifeExpectency = sum(z[1])/len(dataPoints)
	return [birthRate, lifeExpectency]

# Return the name of each country per cluster 

def Countries(clstdPoints, alldata):
	countries = []
	for i, value in enumerate(alldata):  
		if value[1] in clstdPoints:     # if the value is found in the clustered data - the country is added to the countries variable list 
			countries.append(alldata[i][0])
	return countries	

# Function that calculates the sum of squared distance per cluster 

def calcsumSq(centroid, dataPoints):
	distances = [calcDist(centroid, d) for d in dataPoints]
	return sum(distances) #unrounded as the sum of the squared distance can affect the accuracy of where a datapoint will be clustered 

#====
# 2. Initialisation procedure

# Requesting the number of clusters
noClusters = int(input("\nNumber of clusters: "))
# Requesting the number of iterations 
noIterations = int(input("Number of iterations: "))

# The data is read in from a CSV file - this file can be updated to another file if required 

allData = readCSV("data2008.csv")
dataPoints = [column[1] for column in allData] #create a list that contains only the birth rate and life expectency

# The initial centroids are randomly generated 

centroids = random.sample(dataPoints, noClusters)

#====
# 3 Implement the K-means algorithm, using appropriate looping

# Variable for storing the iterations

iterations = 0

# Variable used to store the previous value of the sum of square distance (in order to later calculate convergence)

preIts = 0 

print("-------------------------------------") 
print("Sum of squared distance per iteration: ")

while iterations <= noIterations: #while loop continues until convergence or it runs through the requested number of iterations 

	# Counting each iteration

	iterations += 1

	# The closest point to each centroid is added here 

	minDis = [[] for i in range(noClusters)]
	
	# cycles through each datapoint 

	for dp in dataPoints:

		#Variable to store the squared distance of each point to the centroid 

		sqDistances = []

		# adding the distance of each data point to each centroid 
		for i in range(noClusters):
			sqDistances.append(calcDist(centroids[i], dp))

			#Adding new points to each centroid after an iteration is completed  
		for i, value in enumerate(sqDistances):
			if value == min(sqDistances):
				minDis[i].append(dp)

	# calculation of the new centroids per iteration
    
	for i in range(noClusters):
		centroids[i] = avDistance(minDis[i])

	# For each cluster, calculate the object function and print out the value
  
	print("\nIteration:", iterations , "\n")
    
	sdTotal = 0 # store the total objective function of each iteration here   
    
	for i in range(noClusters):
		sumSq = calcsumSq(centroids[i], minDis[i])
		print ("Cluster", i+1 ,"sum of squared distance: ", round(sumSq,2))
		sdTotal += sumSq
	print("Total: ", round(sdTotal,2))		    

	# End if the iteration limit has been reached or if the program has converged 
	# Convergence is defined in this case as the change in the sum of squared distance, from 1 iteration to another, being less than 0.5 

	if abs(sdTotal - preIts) < 0.5:
		print("\nConvergence has been reached!")
		break
	elif iterations == noIterations:
		print("\nThe required iterations have been completed!")	
		break  	
	preIts = sdTotal

#====
# 4 Printing out the results

print("-------------------------------------") 
print("\nNumber of Countries per Cluster: \n")

for i in range(noClusters):
	print("Cluster " , str(i+1) + ":", len(minDis[i]), "countries.")

print("-------------------------------------") 
print("\nCountries Belonging to Each Cluster: \n")

for i in range(noClusters):
        print("\nCluster "+ str(i+1) + ": \n" "\n",Countries(minDis[i], allData))

print("-------------------------------------") 
print("\nThe mean Life Expectancy and Birth Rate for each cluster: \n")

for i in range(noClusters):
        print ("Cluster " + str(i+1) + ": Life Expectancy: " + str(round(centroids[i][1], 2)) + "| Birth Rate: " + str(round(centroids[i][0], 2)))

