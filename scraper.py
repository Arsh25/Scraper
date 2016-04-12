#! /usr/bin/env python2

"""
	Arsh Chauhan
	04/11/2016
	scraper.py: Scrapes an onlien database using GET requests.
	Made for a UAF Cyber Security Club exercise 
"""

import urllib2
import json
from StringIO import StringIO
import time # For benchmarking 

"""
	scrape: Scrape Mike's Lawlorg server for all employees
	Pre: list must be a valid list
	Post: Returns a python dict. 
"""
def scrape (list):
	database = []
	for ID in list:
		url = 'https://nullify.cc/lawlorg/?search='+ str(ID) 
		response = urllib2.urlopen(url)
		database.insert (ID,json.load(response))
		print (ID)
	return database

if __name__ == '__main__':
	startTime = time.time()
	ids = [223239, 223238, 223634, 223635]
	database = scrape(ids)
	print (database)
	employees = open('employees.json','w')
	json.dump(database,employees)
	endTime = time.time()
	print ('Run Time: ') + str(endTime - startTime)
