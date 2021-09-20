from bs4 import BeautifulSoup
import requests
import json
import time
import pyautogui


#api covid
page = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
soup = BeautifulSoup(page.text, 'html.parser')
container = soup.findAll("div", {"class": "maincounter-number"})

cases = container[0].text.strip()
deaths = container[1].text.strip()
recovered = container[2].text.strip()

brasil = (" O total de casos no Brasil: \n" + \
          " Casos confirmados: " + cases + "\n" + \
          "✝ Óbitos: " + deaths+"\n" + \
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

url = "https://hooks.zapier.com/hooks/catch/10934489/b6srkfc"
data = {'value1': brasil, 'value2': mundi}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)

print("Sleeping for 6 hours")
time.sleep(7200)

#api clima-tempo

# tolkien = 'e28c15b24acee4755e78e314c3ee096b'
# tipoConsulta = 1

# if tipoConsulta == 1:
#     ##não pedir o nome da cidade, enviar por default

## "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=your-app-token"

token = 'e28c15b24acee4755e78e314c3ee096b'
city = '6037'

url = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/' + city +'/current?token=' + token
response = requests.request('GET', url)
retorno = json.loads(response.text)
# print(retorno)

for key in retorno:
  print(key + ': ' + str(retorno[key]))

for key in retorno['data']:
  print(key + ': ' + str(retorno['data'][key]))
