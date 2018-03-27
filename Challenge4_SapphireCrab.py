import matplotlib.pyplot as mplot
import numpy as np
import glob

try:
	userInput = float(input('How many Neighbors would you like to sample?: '))
except ValueError:
	float(input('Error! -- PLEASE ENTER ONLY NUMBERS!: '))

migrationData = glob.glob('C:/Users/**/SapphireCrab/data.csv', recursive=True)
migrationData = open(migrationData, 'r')
migrationData = migrationData.read()
migrationData = migrationData.split('\n')

mapData = glob.glob('C:/Users/**/SapphireCrab/us_outline.csv', recursive=True)
mapData = open(mapData, 'r')
mapData = mapData.read()
mapData = mapData.split('\n')

data = []
usMap = []

for info in migrationData:
	info = info.split(',')
	data.append(info)

for info in mapData:
	info = info.split(',')
	usMap.append(info)

print(data)

# x, y, v =

# x = horizontal grid position
# y = vertical grid position
# v = population change reconstructed

# mplot.scatter(x, y, c=v, cmap='viridis')
# mplot.show()
