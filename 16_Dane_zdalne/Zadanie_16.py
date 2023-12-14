# Pobrać dane z https://restcountries.com/v3.1/name/Poland?fullText=true; Wyświetlić podstawowe informacje (np. il. mieszkańców, waluta itp.)
# Stworzyć skrypt który z linii poleceń przyjmie nazwę kraju i dal niego wyświetli w/w dane

import requests
from pprint import pprint

url = "https://restcountries.com/v3.1/name/Poland?fullText=true"
response = requests.request(method="GET", url=url)
data = response.json()[0]
pprint(data.keys())
# keys literowanie po slowniku
print(f'Ludnosc:\t\t{data["population"]}')
print(f'Powierzchnia:\t{data["area"]}')
print(f'Waluta:\t\t\t{list(data["currencies"].keys())[0]}')
print(f'Stolica:\t\t{data["capital"][0]}')

#  to jest przykład dla jednego kraju prosto z linku tylko w temrinalu wysyakuje Polska w Zadanie 16 p2 jest dla wszytstkich krajów