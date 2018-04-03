'''
	Name: James Jacob Shaver
	ID: SapphireCrab
	Email: jjshaver@go.olemiss.edu
	Program Source File Name: SapphireCrab.py
	Last Edit Date: 2 April 2018
	Course Information: CSci 343
	Program Description:
	Sources Consulted:
	Honor Code Statement: In keeping with the honor code policies of the
	University of Mississippi, the School of Engineering, and the Department of
	Computer and Information Science, I affirm that I have neither given nor
	received assistance on this programming assignment. This assignment
	represents my individual, original effort.
		...My Signature is on File.
	'Lasciate ogne speranza, voi ch'intrate'
'''
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as mplot
import numpy as np
import glob
import csv

try:
	userInput = float(input('How many Neighbors would you like to sample?: '))
except ValueError:
	float(input('Error! -- PLEASE ENTER ONLY NUMBERS!: '))

migrationData = glob.glob('C:/Users/**/SapphireCrab/data.csv', recursive=True)

for moveData in migrationData:
	mapData = open(moveData, 'r')
	read = csv.reader(mapData)
	data = list(read)

mapData = glob.glob('C:/Users/**/SapphireCrab/us_outline.csv', recursive=True)

for cartogropher in mapData:
	cData = open(cartogropher, 'r')
	read = csv.reader(cData)
	mData = list(read)

x = []
y = []
v = []
avg = 0

for i in range(0, 194):
	for k in range(0, 120):
		distance = []
		for j in data:
			a = [i, k]
			b = [int(j[0]), int(j[1])]
			dist = math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))
			distance.append([dist, np.float64(j[2])])
		distance = sorted(distance, key=lambda val: val[0])
		distance = distance[0: int(userInput)]
		for l in distance:
			avg += l[1]
		avg = avg / userInput
		v.append(avg)
		x.append(i)
		y.append(k)

xLine = []
yLine = []

for row in mData:
	xLine.append(float(row[0]))

for col in mData:
	yLine.append(float(col[1]))

mplot.title('Domestic Migration in the United States of America')
mplot.plot(xLine, yLine, color='black', linestyle='-')
mplot.scatter(x, y, c=v, cmap='viridis')
mplot.show()
