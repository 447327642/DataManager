
###
#
#	Pulls down and manages data.
#
#	Right now I just want to be able to abstract downloading a historical CSV
#	for a single company. Currently using Google finance.
#
###

import requests
import csv

class DataManager:

	def __init__(self):
		pass

	def downloadData(self, symbol, range=None):
		""" 
		Return a csv object with symbol data.
		csv object is iterable by csv.reader
		"""

		#Holds the base Google finance URL
		base_data_url = "http://www.google.com/finance/historical?output=csv&q="
		#Create full URL for downloading desired data
		download_url = base_data_url + symbol

		if (range != None):
			download_url = download_url + "&startdate=" + range[0] + "&enddate=" + range[1]

		#Download
		csv = (requests.get(download_url)).content
		csv = csv.split() #format string to be iterable for csv.reader

		return csv

	def getData(self, symbol):
		"""
		Basic get function. Returns data.
		"""
		pass

if __name__ == "__main__":

	datamanager = DataManager()
	spycsv = datamanager.downloadData("AAPL")

	csvreader = csv.reader(spycsv)
	for row in csvreader:
		print row

