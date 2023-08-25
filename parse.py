#!/usr/bin/python3
#parse.py

import urllib3

http = urllib3.PoolManager()

url = 'http://www.megacorpone.com'

response = http.request('GET', url)
print(response.data.decode('utf-8'))