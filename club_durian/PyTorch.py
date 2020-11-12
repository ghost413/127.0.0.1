'''
	Name: James Jacob Shaver
	Email: jjshaver@go.olemiss.edu
	Program Source File Name: README.md
	Last Edit Date: 11 November 2020
	Course Information: CSci 487
	Program Description: This is a readme file on how to use my NeuralNetwork
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

import torch, open3d as o3d, matplotlib.pyplot as plt, random, math, numpy as np
from torchvision import transforms, datasets
from path import Path 

# mesh = o3d.io.read_triangle_mesh("F:/3D Printer Files/PyTorchFiles/Yorik_skull.stl")
# pointCloud = mesh.sample_points_poisson_disk(100000)

# o3d.visualization.draw_geometries([mesh])
# o3d.visualization.draw_geometries([pointCloud])

train = datasets.MNIST("", train=True, download=True,
						transform = transforms.Compose([transforms.ToTensor()]))

test = datasets.MNIST("", train=False, download=True,
						transform = transforms.Compose([transforms.ToTensor()]))

trainSet = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testSet = torch.utils.data.DataLoader(test, batch_size=10, shuffle=True)

for data in trainSet:
	print(data)
	break

x, y = data[0][0], data[1][0]
print(y)

plt.imshow(data[0][0].view(28,28))
plt.show()

total = 0
counterDict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for data in trainSet:
	Xs, ys = data
	for y in ys:
		counterDict[int(y)] += 1
		total+=1

	print(counterDict)

for i in counterDict:
	print(f"{i}: {counterDict[i]/total*100}")
