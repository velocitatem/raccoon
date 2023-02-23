# read the file malicous.csv
# this is a list of lists
# each item is like this: [malicious prompt, expected malicous response]

# build a CLI application to test a prompt to see if it is susceptible to malicious input
# the application should take a prompt as input and return percentage of malicious input that passed is detected

import json
import sys
import os
import subprocess

# read the file malicous.csv
# this is a list of lists
# each item is like this: [malicious prompt, expected malicous response]
import csv
def readMaliciousFile():
    # read the file
    # return a list of lists
    # each item is like this: [malicious prompt, expected malicous response]
    with open('malicious.csv', 'r') as f:
        reader = csv.reader(f)
        malicious = list(reader)
    # ignore first row
    malicious = malicious[1:]
    return malicious
data = readMaliciousFile()

import requests
def runPrompt(prompt):
    # send a get request to localhost:3042/new/person/:introduction
    # the introduction is the prompt
    r = requests.get('http://localhost:3042/capital/' + prompt)
    return r.json().get('response')



def compare(expected, recieved):
    # print a grpahic of the comparison
    # use colors
    # both params are strings
    # return a boolean
    # if the strings are the same, return true
    # if the strings are different, return false
    print('------------------------------')
    print('expected: ' + expected)
    print('recieved: ' + recieved)
    print('------------------------------')
    res = expected == recieved
    print('result: ' + str(res))
    return res


# get the prompt from the user

# get the number of malicious inputs
malicious_inputs = len(data)

# get the number of malicious inputs that passed
malicious_inputs_passed = 0

# loop through the malicious inputs
for malicious_input in data:

    # get the malicious input
    malicious_input, expected_malicious_response = malicious_input

    print("Testing malicious input: " + malicious_input)
    # run the prompt with the malicious input
    malicious_response = runPrompt(malicious_input)
    # try to convert malicious_response to a string
    try:
        malicious_response = str(malicious_response)
    except:
        malicious_response = ""


    # check
    if compare(expected_malicious_response, malicious_response):
        malicious_inputs_passed += 1


# calculate the percentage of malicious inputs that passed
percentage_malicious_inputs_passed = malicious_inputs_passed / malicious_inputs

# print the percentage of malicious inputs that passed
print("Percentage of malicious inputs that passed: " + str(percentage_malicious_inputs_passed))
