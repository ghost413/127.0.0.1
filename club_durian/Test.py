import requests
count = 5

url = 'https://thingiverse.com/thing:' + str(count) + '/zip'

#use the 'headers' parameter to set the HTTP headers:
x = requests.head(url)

print(x.headers)