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

#Tempo
token = 'e28c15b24acee4755e78e314c3ee096b'
city = '6037'

url = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/' + city +'/current?token=' + token
response = requests.request('GET', url)
retorno = json.loads(response.text)
# print(retorno)

# for key in retorno:
#  print(key + ': ' + str(retorno[key]))

cidadeNome = retorno['name']
cidadeEstado = retorno['state']
temperatura = retorno['data']['temperature']
condicao = retorno['data']['condition']
sensacao = retorno['data']['sensation']
velocidadeVento = retorno['data']['wind_velocity']
dia = retorno['data']['date']


clima = ("O clima em " + cidadeNome + "-" + cidadeEstado + " : " + dia + "\n" + \
          "Temperatura = " + temperatura + "ºC \n" + \
          "Sensação térmica = " + sensacao + "ºC \n" + \
          "Ventos de = " + velocidadeVento + "km/h \n" + \
          "O dia está = " + condicao + " .\n\n")


# for key in retorno['data']:
#   print(key + ': ' + str(retorno['data'][key]))
  
url = "https://hooks.zapier.com/hooks/catch/10934489/b6srkfc"
data = {'value1': brasil, 'value2': clima, 'value3': mundi}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)

print("Sleeping for 2 hours")
time.sleep(7200)

##abrir o twitter e dar f5 na pagina