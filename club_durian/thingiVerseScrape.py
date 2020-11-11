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

import os, requests
from tqdm import tqdm
count = 5503
chunk = 1024
url = 'https://thingiverse.com/thing:' + str(count) + '/zip'
req = requests.get(url, stream=True)
size = int(req.headers.get('Content-Length', 0))
filename = url.split('- Thingiverse')[-1]
print(filename)
progress = tqdm(req.iter_content(chunk), f'Downloading {filename}', 
			total=size, unit='B', unit_scale=True, unit_divisor=1024)
with open('filename', 'wb') as zip:
		for data in progress:
			zip.write(req.content)
			progress.update(len(data))
