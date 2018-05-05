'''
	Name: James Jacob Shaver
	ID: SapphireCrab
	Email: jjshaver@go.olemiss.edu
	Program Source File Name: SapphireCrab.py
	Last Edit Date: 16 April 2018
	Course Information: CSci 343
	Program Description:
	Sources Consulted:
	Honor Code Statement: In keeping with the honor code policies of the
	University of Mississippi, the School of Engineering, and the Department of
	Computer and Information Science, I affirm that I have neither given nor
	received assistance on this programming assignment. This assignment
	represents my individual, original effort.
		...My Signature is on File.

			'Was wir für uns selbst tun, stirbt mit uns.
	Was wir für andere und die Welt tun, bleibt und ist unsterblich.'
'''
import numpy as np
import glob

newLine = []
yAxis = []
xAxis = []

# Getting Data points for the Map

setiData = glob.glob(
	'C:/Users/**/SapphireCrab/SapphireCrab.csv', recursive=True)

# loop through recursive call for files and open/split/and pop last line
# aslo setting newLine with all the information
for path in setiData:
	with open(path) as data:
		line = data.read().split('\n')
		if line[-1] == '':
			line.pop()
		for info in line:
			nInfo = info.split(',')
			newLine.append(nInfo)

# looping through newLine to extract x and y values and append
for i in newLine:
	i[0] = np.float64(i[0])
	i[2] = np.float64(i[2])
	xAxis.append(i[0])
	yAxis.append(i[2])


# function call to get x values
def getXData():
	return np.float64(xAxis)


# function call to get y values
def getYData():
	return np.float64(yAxis)
