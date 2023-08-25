#!/usr/bin/python3
#parse.py

import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import socket
import requests

host = "192.168.51.68"
port = 8080
url = urlopen("http://www.megacorpone.com:" + str(port) + "/crawling")

page = url.read()
soup = BeautifulSoup(page, features="html.parser")

print(soup.get_text())
