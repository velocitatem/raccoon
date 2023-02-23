import requests
def runPrompt(prompt):
    r = requests.get('http://localhost:3042/capital/' + prompt)
    return r.json().get('response')
