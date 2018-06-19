import sys, requests, os

'''
conn = psycopg2.connect(
		database = "requestInfo",
		user = "postgres",
		password = "lucky90322@",
		host = "127.0.0.1",
		port = "5432"
		)

cursor = connection.cursor()
'''
# r = requests.post(ip, data={'keywords':sys.argv[1]})
os.system('python3 function.py ' + sys.argv[1])
