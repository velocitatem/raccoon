import requests
def runPrompt(prompt):
    r = requests.get('http://localhost:3042/food/' + prompt)
    return r.json().get('response')
