import os, re, sys, threading, mysql.connector
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from flask import Flask, request
import json

'''Constant url'''
url = 'https://www.youtube.com/results?search_query='
CRAWLER_HOST = os.environ['CRAWLER_HOST'] 
CRAWLER_USER = os.environ['CRAWLER_USER']
CRAWLER_PASSWORD = os.environ['CRAWLER_PASSWORD']

app = Flask(__name__)

@app.route('/crawler', methods=['GET'])
def crawler():
	inputs = request.args.get('text')

	'''Driver'''
	
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')
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

	conn = mysql.connector.connect(host = CRAWLER_HOST, database = 'Crawler', user = CRAWLER_USER, password = CRAWLER_PASSWORD)
	cursor = conn.cursor()
	query = "INSERT INTO result(keyword, url, title) VALUES(%s, %s, %s)"	
	for i in range(len(rowdata)-1):
		args = (inputs, urldata[i], rowdata[i])
		cursor.execute(query, args)
		conn.commit()

	return json.dumps(rowdata)

app.run(debug = True, host='0.0.0.0')
