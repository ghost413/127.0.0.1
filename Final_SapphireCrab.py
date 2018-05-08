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
import glob
# import aStarSearch as aStar

myNetwork = glob.glob('C:/Users/**/myNetwork.csv', recursive=True)

count = 0
userInput = float(input('\nHow many times do you' +
				' want to run the Search algorithm?: '))
sInfo = []


def search(x, y):
	if grid[x][y] == 2:
		print('Solved... This is a Maze!')
		sInfo.append(1)
		return True
	elif grid[x][y] == 1:
		print('Wall! at %d, %d' % (x, y))
		return False
	elif grid[x][y] == 3:
		print('Visiting %d, %d' % (x, y))
		return False
	print('Not a Maze!')
	grid[x][y] = 3
	if ((x < len(grid) - 1 and search(x + 1, y))
		or (y > 0 and search(x, y - 1))
		or (x > 0 and search(x - 1, y))
		or (y < len(grid) - 1 and search(x, y + 1))):
		return True
	return False


while count != userInput:
	seq = []
	for i in range(5):
		seq.append((random.randint(0, 1)))
		for k in range(4):
			seq.append((random.randint(0, 1)))

	if seq[0] == 0 and seq[-1] == 0:
		seq[-1] = 2
		grid = [seq[:5], seq[5:10], seq[10:15], seq[15:20], seq[20:]]
		count += 1
		print(grid)
	else:
		print('A maze this is not... Skipping')
	search(0, 0)

print(sInfo)
