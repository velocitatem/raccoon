import json
import sys
import os
import subprocess
from run import runPrompt

# read the file malicous.csv
# each item is like this: [malicious prompt, expected malicous response]
import csv
def readMaliciousFile():
    # each item is like this: [malicious prompt, expected malicous response]
    with open('malicious.csv', 'r') as f:
        reader = csv.reader(f)
        malicious = list(reader)
    # ignore first row
    malicious = malicious[1:]
    return malicious
data = readMaliciousFile()






def compare(expected, recieved):
    print('------------------------------')
    print('expected: ' + expected)
    print('recieved: ' + recieved)
    print('------------------------------')
    res = expected == recieved
    print('result: ' + str(res))
    return res


malicious_inputs = len(data)
malicious_inputs_passed = 0

for malicious_input in data:

    malicious_input, expected_malicious_response = malicious_input

    print("Testing malicious input: " + malicious_input)
    malicious_response = runPrompt(malicious_input)
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
