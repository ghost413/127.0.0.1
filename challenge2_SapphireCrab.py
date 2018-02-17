''' 
	Name: James Jacob Shaver 
	ID: SapphireCrab
	Email: jjshaver@go.olemiss.edu
	Program Source File Name: main.py
	Last Edit Date: Sunday 23 February 2018
	Course Information: CSci 343
	Program Description: 
	Sources Consulted: 
	Honor Code Statement: In keeping with the honor code policies of the
	University of Mississippi, the School of Engineering, and the Department of
	Computer and Information Science, I affirm that I have neither given nor
	received assistance on this programming assignment. This assignment
	represents my individual, original effort.
		...My Signature is on File.
''' 
import numpy as np
import matplotlib.pyplot as mplot
import glob
import re

class SentimentChecker()
	
	data = {}
	signum = []

	def feelings(mS, file)

		for words in file:
			if not words.isalpha():
				continue
			if len(words) == 1:
				continue
		

def main()

	mS = open('sentiment_lex.csv', 'r')
	mS = mS.read()
	mS = mS.split('\n')

	fileA = glob.glob('C:/Users/**/a*script.txt', recursive = True)
	fileA = re.sub(r'\W+', ' ', fileA)
	fileA = fileA.split(' ')
	fileB = glob.glob('C:/Users/**/b*script.txt', recursive = True)
	fileB = re.sub(r'\W+', ' ', fileB)
	fileB = fileB.split(' ')

	SentimentChecker.feelings(mS, fileA)
	SentimentChecker.feelings(mS, fileB)

	mplot.