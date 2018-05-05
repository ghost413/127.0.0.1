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
import matplotlib.pyplot as mplot

newLine = []
frequency = []
xAxis = []
yAxis = []
slope = []
coor = []

(channel_x, channel_y, channel_1x, channel_1y,
	channel_2x, channel_2y, channel_3x, channel_3y,
	channel_4x, channel_4y) = [], [], [], [], [], [], [], [], [], []

setiData = glob.glob(
	'C:/Users/**/SapphireCrab/SapphireCrab.csv', recursive=True)

# loop through recursive call for files and open/split/and pop last line
for path in setiData:
	with open(path) as data:
		line = data.read().split('\n')
		if line[-1] == '':
			line.pop()
	# loop through the now opened and split csv file and split again
	for info in line:
		nInfo = info.split(',')
		newLine.append(nInfo)
		frequency.append(nInfo[1])
		frequency = list(set(frequency))

# loop through the newly aquired info and 
# check if they match unique list and append
for info in newLine:
	info[0] = np.float64(info[0])
	info[2] = np.float64(info[2])
	if info[1] == frequency[0]:
		channel_x.append(info[0])
		channel_y.append(info[2])
		coor = np.corrcoef(channel_x, channel_y)[0, 1]
		if abs(coor) >= 0.7:
			slope.append((np.std(channel_x,) / np.std(channel_y)) * coor)
	if info[1] == frequency[1]:
		channel_1x.append(info[0])
		channel_1y.append(info[2])
		coor = np.corrcoef(channel_1x, channel_1y)[0, 1]
		if abs(coor) >= 0.7:
			slope.append((np.std(channel_1x,) / np.std(channel_1y)) * coor)
	if info[1] == frequency[2]:
		channel_2x.append(info[0])
		channel_2y.append(info[2])
		coor = np.corrcoef(channel_2x, channel_2y)[0, 1]
		if abs(coor) >= 0.7:
			slope.append((np.std(channel_2x,) / np.std(channel_2y)) * coor)
	if info[1] == frequency[3]:
		channel_3x.append(info[0])
		channel_3y.append(info[2])
		coor = np.corrcoef(channel_3x, channel_3y)[0, 1]
		if abs(coor) >= 0.7:
			slope.append((np.std(channel_3x,) / np.std(channel_3y)) * coor)
	if info[1] == frequency[4]:
		channel_4x.append(info[0])
		channel_4y.append(info[2])
		coor = np.corrcoef(channel_4x, channel_4y)[0, 1]
		if abs(coor) >= 0.7:
			slope.append((np.std(channel_4x,) / np.std(channel_4y)) * coor)
	# xAxis.append(info[0])
	# yAxis.append(info[2])

# Plot all the scatter points and lines
mplot.title('SETI Radio Frequencies (MHz)')
mplot.xlabel('Time (ms)')
mplot.ylabel('Signal Intensity')
mplot.scatter(channel_x, channel_y, c='blue', marker='o')
mplot.scatter(channel_1x, channel_1y, c='orange', marker='o')
mplot.scatter(channel_2x, channel_2y, c='violet', marker='o')
mplot.scatter(channel_3x, channel_3y, c='indigo', marker='o')
mplot.scatter(channel_4x, channel_4y, c='red', marker='o')
mplot.show()
