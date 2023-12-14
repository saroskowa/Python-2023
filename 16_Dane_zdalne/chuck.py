import requests
from pprint import pprint

url = "https://api.chucknorris.io/jokes/random"
response = requests.request(method="GET", url=url)

pprint(response.json())

# print()
# print(25*"*")
# print()
# te printy pokazuje jedyne dekoracyjne gwiazdki

print(response.json()['value'])