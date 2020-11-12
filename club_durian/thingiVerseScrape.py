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

import os, requests, time, zipfile
from tqdm import tqdm

class ZipDownloader():

	def getZipFile(self, mCount, mUrl):

		chunk = 1024
		url = mUrl
		count = mCount
		path = os.getcwd() + '/Zip Files/'
		try:
			req = requests.get(url, stream=True)
			size = int(req.headers['content-length'])
			with open(str(path) + str(count) + '.zip' ,'wb') as zip:
				for data in tqdm(req.iter_content(chunk), f'Downloading {count}', total=size, 
								unit='KB', unit_scale=True, unit_divisor=1024):
					zip.write(req.content)
					time.sleep(1)
			print('Download Complete!')

		except requests.exceptions.HTTPError as errh:
			print("Http Error: ", errh)
			raise errh
		except requests.exceptions.ConnectionError as errc:
			print("Error Connecting:", errc)
			raise errc
		except requests.exceptions.Timeout as errt:
			print("Timeout Error:", errt)
			raise errt
		except requests.exceptions.RequestException as err:
			print("Something Else Went Wrong", err)
			raise err

class cleanFiles():

	def extractFile(self, zPath, zCount):
		path = zPath
		count = zCount

		zipFile = zipfile.ZipFile(str(path), mode='r')
		print('Extracting ' + count + '.zip')
		zipFile.extractall()
		print('Extraction done!')
		zipFile.close()


if __name__ == '__main__':
	count = 5503
	download = ZipDownloader()
	while count <= 5506:
		url = 'https://thingiverse.com/thing:' + str(count) + '/zip'
		download.getZipFile(count, url)
		count += 1
