#! /usr/bin/env python2

"""
	Arsh Chauhan
	04/11/2016
	Edited: 04/12/2016
	filter.py: Removes empty entires from a JSON file
	Made for a UAF Cyber Security Club exercise 
"""

import json
import time

def search(employees,department):
	ITEmployees = []
	for person in employees:
		if person["4Department"] == department:
			ITEmployees.append(person)
	return ITEmployees


if __name__ == '__main__':
	startTime  =  time.time()
	with open("employees.json") as jsonFile:
		rawDatabase = json.load(jsonFile)
	ITEmployees = search(rawDatabase,"Information Technology")
	Management = search (rawDatabase,"Management")
	HREmployees = search(rawDatabase,"Human Resources")
	securityEmployees = search (rawDatabase,"Security")
	janiorialEmployees = search (rawDatabase, "Janitorial")
	IT = open('informationTechnology.json','w')
	Mng = open("management.json",'w')
	HR = open('humanResources.json','w')
	Sec = open('security.json','w')
	Janitors = open('janitorial.json','w')
	json.dump(ITEmployees,IT)
	json.dump(Management,Mng)
	json.dump(HREmployees,HR)
	json.dump(securityEmployees,Sec)
	json.dump(janiorialEmployees,Janitors)
	endTime = time.time()
	print("Run Time: ") + str(endTime - startTime)