import requests
def runPrompt(prompt):
    r = requests.get('http://localhost:3000/help?issue=' + prompt)
    return r.json().get('response')
