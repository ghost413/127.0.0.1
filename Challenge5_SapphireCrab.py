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
import numpy
import glob
import csv

setiData = glob.glob(
	'C:/Users/**/SapphireCrab/SapphireCrab.csv', recursive=True)

for data in setiData:
	sData = open(data, 'r')
	read = csv.reader(sData)
	rSignal = list(read)

print(rSignal)
