import requests
import csv

def getCSV(url):
	try:
		data = []
		with requests.Session() as s:
			download = s.get(url,timeout=5) # Gets the csv file download
			decoded_content = download.content.decode('utf-8')
			cr = csv.reader(decoded_content.splitlines(), delimiter=',') # Read through the downloaded CSV
			my_list = list(cr) # Converts the object into a list variable type
			for row in my_list:
				data.append(row)
		return data
	except:
		return False

def getJSON(url):
	try:
		r = requests.get(url,timeout=5) # Sends the request to the API
		try: # In case an API failure occurs, prints the response from the api
			return r.json() # Converts the API response into a consummable JSON format
		except: 
			return False
	except:
		return False