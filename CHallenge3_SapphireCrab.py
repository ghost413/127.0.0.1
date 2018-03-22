'''
	Name: James Jacob Shaver
	ID: SapphireCrab
	Email: jjshaver@go.olemiss.edu
	Program Source File Name: SapphireCrab.py
	Last Edit Date: 9 March 2018
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

import numpy as np
import matplotlib.pyplot as mplot
import glob
from PIL import Image

file = glob.glob('C:/Users/**/starbucks_*.jpg', recursive=True)

images = []

userInput = float(input('Please input a Deviation between 0 and 255: '))
if (userInput > 255 or userInput < 0):
	userInput = float(input('Invaid. Please input a number between 0 and 255: '))

for jpg in file:
	image = Image.open(jpg)
	image = np.float64(image)
	images.append(image)

avgImg = images[0]

stdD = [0, 0, 0]

for i in range(1, len(images)):
	avgImg += images[i]

avgImg /= len(images)

for i in range(0, len(images)):
	stdD += (images[i] - avgImg)**2

stdD /= (len(images) - 1)

stdD = np.sqrt(stdD)

for row in range(0, len(avgImg)):
	for col in range(0, len(avgImg[row])):
		if (stdD[row][col] > userInput).any():
			avgImg[row][col] = [255, 0, 0]

avgImg = np.clip(avgImg, 0, 255)

avgImg = np.uint8(avgImg)

mplot.imshow(avgImg)
mplot.show()
