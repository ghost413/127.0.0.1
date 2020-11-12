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

import requests, open3d as o3d, os
# count = 5503
# path = os.getcwd() + '/Zip Files/'
# # url = 'https://thingiverse.com/thing:5503'

# # #use the 'headers' parameter to set the HTTP headers:
# # x = requests.head(url)

# # print(x.headers)

# # mesh = o3d.io.read_triangle_mesh("F:/3D Printer Files/PyTorchFiles/Yorik_skull.stl")
# # pointCloud = mesh.sample_points_poisson_disk(100000).ToTensor()
# # print(pointCloud)

# # o3d.visualization.draw_geometries([mesh])
# # o3d.visualization.draw_geometries([pointCloud])
# url = 'https://thingiverse.com/thing:' + str(count) + '/zip'
 
# r = requests.get(url, stream=True)
 
# with open(str(path) + str(count) + ".zip", "wb") as zip:
#     zip.write(r.content)

class add():
	num1 = 0
	num2 = 0
	def addition(self, n1, n2):
		num1 = n1
		num2 = n2
		return num1 + num2

if __name__ == '__main__':
	c = add()
	print(c.addition(2,3))
