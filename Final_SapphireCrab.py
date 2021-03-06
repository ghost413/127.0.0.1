'''
	Name: James Jacob Shaver
	ID: SapphireCrab
	Email: jjshaver@go.olemiss.edu
	Program Source File Name: main.py
	Last Edit Date: Sunday 31 January 2018
	Course Information: CSci 343
	Program Description:
	Sources Consulted:
	https://www.nationalgeographic.com/animals/invertebrates/b/blue-crab/,
	Life History of the Blue Crab by E.P. Churchill Jr.
	Honor Code Statement: In keeping with the honor code policies of the
	University of Mississippi, the School of Engineering, and the Department of
	Computer and Information Science, I affirm that I have neither given nor
	received assistance on this programming assignment. This assignment
	represents my individual, original effort.
		...My Signature is on File.

			'Was wir für uns selbst tun, stirbt mit uns.
	Was wir für andere und die Welt tun, bleibt und ist unsterblich.'
'''
import neuro
import random
import os

# inputs = open('myNetwork.csv', 'r')
# inputs = inputs.read()
# inputs = inputs.split('\n')
# if inputs[-1] == '':
# 	inputs.pop()

# newT = []
# targets = open('myTest.csv', 'r')
# targets = targets.read()
# targets = targets.split('\n')
# if targets[-1] == '':
# 	targets.pop()
# for i in targets:
# 	newT.append(i.split(','))
# 	print(float(newT))



reps = 1000
network = []
netowrk = neuro.setup_network(inputs)
neuro.train(network, inputs, targets, reps)
neuro.writeNetworkToFile('myNetwork.net', network)

count = 0
myGrid = open('myNetwork.csv', 'w+')


def search(x, y):
		if grid[x][y] == 2:
			print('Solved... This is a Maze!')
			return True
		elif grid[x][y] == 1:
			print('Wall! at %d, %d' % (x, y))
			return False
		elif grid[x][y] == 3:
			print('Visiting %d, %d' % (x, y))
			return False
		print('Visiting %d, %d' % (x, y))
		grid[x][y] = 3
		if ((x < len(grid) - 1 and search(x + 1, y))
			or (y > 0 and search(x, y - 1))
			or (x > 0 and search(x - 1, y))
			or (y < len(grid) - 1 and search(x, y + 1))):
			return True
		return False


while count != 200:
	seq = []
	newSeq = []
	for i in range(5):
		seq.append((random.randint(0.0, 1.0)))
		for k in range(4):
			seq.append((random.randint(0.0, 1.0)))
	if seq[0] == 0 and seq[-1] == 0:
		for i in seq:
			newSeq.append(float(i))
		grid = [newSeq[0:5], newSeq[5:10], newSeq[10:15], newSeq[15:20], newSeq[20:]]
		count += 1
		
		myGrid.write(str(grid) + '\n')
	else:
		print('A maze this is not... Skipping')
	print(grid)
