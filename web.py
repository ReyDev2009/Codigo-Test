import requests
                
url = ("https://aprendeconalf.es/docencia/python/manual/pandas/")
headers = {'user-agent': 'chrome/108.0.5359.125'}

r = requests.get(url, headers=headers)


file = open("database.txt", "w")
file.write(r.text)
