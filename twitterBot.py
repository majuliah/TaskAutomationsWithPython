from bs4 import BeautifulSoup
import requests
import json
import time


page = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
soup = BeautifulSoup(page.text, 'html.parser')
container = soup.findAll("div", {"class": "maincounter-number"})

cases = container[0].text.strip()
deaths = container[1].text.strip()
recovered = container[2].text.strip()

brasil = (" O total de casos no Brasil: \n" + \
          " Casos confirmados: " + cases + "\n" + \
          " Óbitos: " + deaths+"\n" + \
          " Recuperações: " + recovered + "\n\n")


page = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(page.text, 'html.parser')
container = soup.findAll("div", {"class": "maincounter-number"})

cases = container[0].text.strip()
deaths = container[1].text.strip()
recovered = container[2].text.strip()

mundi = (" O total de casos no Mundo: \n" + \
          " Casos confirmados: " + cases + "\n" + \
          " Óbitos: " + deaths+"\n" + \
          " Recuperações: " + recovered + "\n\n")



print(brasil)
print(mundi)

url = "https://hooks.zapier.com/hooks/catch/10933719/b6sd95u/"
data = {'value1': brasil, 'value2': mundi}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)