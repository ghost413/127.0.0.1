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
import random
import neuro

size = 5
count = 0
grid = []
target = []
inputs = []
reps = 1000
network = []
myGrid = open('myNetwork.csv', 'w+')

while count != 5:
	seq = []
	newSeq = []
	for i in range(5):
		seq.append((random.randint(0.0, 1.0)))
		for k in range(4):
			seq.append((random.randint(0.0, 1.0)))
	if seq[0] == 0 and seq[-1] == 0:
		for i in seq:
			newSeq.append(float(i))
		grid = newSeq[0:5], newSeq[5:10], newSeq[10:15], newSeq[15:20], newSeq[20:]
		count += 1
		inputs.append([newSeq[0:5], newSeq[5:10], newSeq[10:15], newSeq[15:20], newSeq[20:]])
		# myGrid.write(str(grid) + '\n')
		# network = neuro.setup_network(grid)
		# neuro.train(network, grid, target, reps)
		# neuro.writeNetworkToFile('myNetwork.net', network)

	else:
		print('A maze this is not... Skipping')
for i in inputs:
	print(i)
