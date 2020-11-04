import os, requests
from tqdm import tqdm
count = 0
chunk = 1024
url = 'https://thingiverse.com/thing:' + str(count) + '/zip'
req = requests.get(url, stream=True)
size = int(req.head['Content-length'])
with open('F:/Final Project Jank/File' + str(count) + '.zip', 'wb') as zip:
		for data in tqdm(iterable=req.iter_content(chuck_size=chunk), total=size/chunk, unit='KB'):
			zip.write(req.content)
print('Download: ' + str(i) + ' Complete!')
# for i in range(1, 200):
# 	with open('F:/Final Project Jank/File' + str(count) + '.zip', 'wb') as zip:
# 		for data in tqdm(iterable=req.iter_content(chuck_size=chunk), total=size/chunk, unit='KB'):
# 			zip.write(req.content)
# 	print('Download: ' + str(i) + ' Complete!')
# 	count += 1
	
# for i in range (1, 10):
# 	r = requests.get(url, stream=True)
# 	print("thing:" + str(i) + " status: " + str(r.status_code))
# 	if r.status_code == 200:
# 		f = open("thing_" + str(i) + ".zip", "wb")
# 		f.write(r.content)
# 		f.close()