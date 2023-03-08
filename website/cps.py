import json
import sys
import os
import subprocess
def runPrompt(malicious_input):
    pass
# read the file malicous.csv
# each item is like this: [malicious prompt, expected malicous response]
import csv

def readMaliciousFile():
    # each item is like this: [malicious prompt, expected malicous response]
    path = os.path.dirname(os.path.realpath(__file__)) + '/malicious.csv'
    with open(path, 'r') as f:
        reader = csv.reader(f)
        malicious = list(reader)
    # ignore first row
    malicious = malicious[1:]
    return malicious


class Tests():
    def pi(self, result):
        return '3.14159265' in result

tests = {
    'pi': Tests().pi
}



def compare(test, recieved):
    print('------------------------------')
    print('recieved: ' + recieved)
    print('expected: ' + test)
    print('------------------------------')
    # use the tests dictionary to check if the recieved response matches the expected response
    res = False
    if test in tests:
        res = tests[test](recieved)
    print('result: ' + str(res))

    return res




def run(method=runPrompt, extra=None):
    data = readMaliciousFile()
    # read the extra malicious input
    malicious_inputs = len(data)
    malicious_inputs_passed = 0
    # first run the extra malicious input
    print(extra)
    if extra:
        # parse csv string to list of lists
        extra = extra.split('\n') # split by space
        extra = [x.split(',') for x in extra] # split by comma
        # remove empty lists where len not 2
        extra = [x for x in extra if len(x) == 2]
        extra = extra[1:]
        print(extra)

        i = 0
        for item in extra:
            i+=1
            print('running extra malicious input ' + str(i) + ' of ' + str(len(extra)))
            result = method(item[0])
            # the second item is a regex of the expected response
            def compareRegex(res, regex):
                # check if the response matches the regex
                import re
                pattern = re.compile(regex)
                return bool(pattern.match(res.strip()))
            passed = compareRegex(result, item[1])
            if passed:
                malicious_inputs_passed += 1
            yld = (item[0], result, passed, "Unknown")
            print(yld)
            yield yld
    i=0
    for malicious_input in data:

        malicious_input, expected_malicious_response, cause = malicious_input

        # print a header for this trial. Include the number and some form of separators
        print('=========================================')
        print('Trial ' + str(i))
        print('=========================================')
        print("\nTesting malicious input:\n\t" + malicious_input)
        malicious_response = method(malicious_input)
        try:
            malicious_response = str(malicious_response)
        except:
            malicious_response = ""


        # check
        passed =compare(expected_malicious_response, malicious_response)
        if passed:
            malicious_inputs_passed += 1
        yield (malicious_input, malicious_response, passed, cause)
        i+=1


    # calculate the percentage of malicious inputs that passed
    percentage_malicious_inputs_passed = malicious_inputs_passed / malicious_inputs

    # print the percentage of malicious inputs that passed
    print('\n=========================================')
    print('Results')
    print('=========================================\n')
    print("Percentage of malicious inputs that passed: " + str(percentage_malicious_inputs_passed))

    # return the percentage of malicious inputs that passed

if __name__ == '__main__':
    run()
