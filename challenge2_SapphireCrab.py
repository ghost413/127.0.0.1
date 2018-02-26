'''
	Name: James Jacob Shaver
	ID: SapphireCrab
	Email: jjshaver@go.olemiss.edu
	Program Source File Name: main.py
	Last Edit Date: Friday 23 February 2018
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


print('\n\t\tWelcome to the Script Analyzer!')
print('\n\t Which series would you like to view?')
print('\t\t\t\tA or B')
userInput = input()

info = []

if userInput.upper() == 'A':

	fileListA = glob.glob('C:/Users/**/a*script.txt', recursive=True)

	for files in fileListA:
		line = open(files, 'r')
		line = line.read()
		line = re.sub(r'\W+', ' ', line)
		line = line.split(' ')
		info.append(line)

if userInput.upper() == 'B':

	fileListB = glob.glob('C:/Users/**/b*script.txt', recursive=True)

	for files in fileListB:
		line = open(files, 'r')
		line = re.sub(r'W+', ' ', line)
		line = line.split(' ')
		info.append(line)

sentiment = {}
mS = glob.glob('C:/Users/**/sentiment_lex.csv', recursive=True)
for files in mS:
	line = open(files, 'r')
	line = line.read()
	line = line.split('\n')
	if(line[-1] == ''):
		line.pop()
		for things in line:
			things = things.split(',')
			sentiment[things[0]] = float(things[1])
dic = {}

for words in info:
	if words in sentiment.values:
		try:
			dic[words] += 1
		except:
			dic[words] = 1
print(dic)

mplot.bar(range(0), len(sentiment.values), sentiment.values)
mplot.xticks(range(0), len(sentiment.keys), sentiment.keys)
mplot.xlabel('Weekly Sentiment')
mplot.ylabel('Weekly Word Count')
mplot.title('CSci 343 Challenge 2: Script Sentiment')
