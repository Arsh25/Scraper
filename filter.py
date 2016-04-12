#! /usr/bin/env python2

"""
	Arsh Chauhan
	04/11/2016
	filter.py: Removes empty entires from a JSON file
	Made for a UAF Cyber Security Club exercise 
"""

import json
import time

"""
	removeInvalid: Remove invalid employee ID'Security
	Pre: None
	Post: Returns a lst with all empty entries removed. 
"""
def removeInvalid(data,length):
	validEmployees = []
	for index in range(0,length):
		if data[index]:
			validEmployees.append(data[index])
	return validEmployees


if __name__ == '__main__':
	startTime  =  time.time()
	with open("employees.json") as jsonFile:
		rawDatabase = json.load(jsonFile)
	validEmployees = removeInvalid(rawDatabase,len(rawDatabase))
	employeeFile = open('validEmployees.json','w')
	json.dump(validEmployees,employeeFile)
	endTime = time.time()
	print("Run Time: ") + str(endTime - startTime)