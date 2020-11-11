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

import requests
count = 5

url = 'https://thingiverse.com/thing:5503'

#use the 'headers' parameter to set the HTTP headers:
x = requests.head(url)

print(x.headers)
