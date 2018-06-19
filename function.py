import re, sys, threading
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/results?search_query='
html = urlopen(url + sys.argv[1])
bsObj = BeautifulSoup(html.read(), 'html.parser')

bsObj.find('twoColumnWatchNextResults')
