import re, sys, threading, mysql.connector
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
from flask import Flask, request

'''Constant url'''
url = 'https://www.youtube.com/results?search_query='

app = Flask(__name__)

@app.route('crawler', method=['GET'])
def crawler():
	inputs = request.args.get('text')

	'''Driver'''
	driver = webdriver.Chrome('./chromedriver')
	driver.get(url + inputs)
	# driver.get(inputs)

	'''Analyze page source'''
	source = driver.page_source
	data = source.split('<script>')
	driver.quit()

	for i in range(len(data)):
		if data[i].find('twoColumnSearch') != -1:
				data = data[i]
				break

	'''Filting data'''
	data = data[data.find('itemSectionRenderer'):data.find('continuation') - 2]

	urldata = []
	rowdata = []
	urldata = re.findall('/watch.+?"', data)
	for i in range(len(urldata)):
		if urldata[i].find(' ') != -1:
			urldata[i] = urldata[i][:urldata[i].find(' ')]

	rowdata = re.findall('"title":{"accessibility".+?}}', data)
	rowdata = [re.sub('"title".+?"label":', '', x) for x in rowdata]
	rowdata = [re.sub('}}', '', x) for x in rowdata]
	rowdata = [re.sub(r'\\u0026', '', x) for x in rowdata]

	conn = mysql.connector.connect(host = 'localhost', database = 'Crawler', user = 'luckypigeon', password = 'lucky90322')
	cursor = conn.cursor()

	query = "INSERT INTO result(keyword, url, title) VALUES(%s, %s, %s)"
	
	for i in range(len(urldata)):
		cursor.execute(query, inputs, urldata[i], rowdata[i])
		conn.commit()

	return rowdata, urldata

app.run(debug = True)
