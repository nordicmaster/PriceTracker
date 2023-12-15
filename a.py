import requests

res = requests.get('https://raw.githubusercontent.com/nordicmaster/CodeExamples/master/books%20to%20read.txt')
print(res.text)