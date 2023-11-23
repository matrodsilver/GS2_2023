from pushbullet import Pushbullet
import requests
import time

def pegarValores():
  urlTSultimoResultado = f'https://api.thingspeak.com/channels/2349078/feeds.json?results=1'

  resposta = requests.get(urlTSultimoResultado)

  if resposta.status_code == 200:
    return resposta.json()
  else:
    print('Erro na requisição')
    return {}

def avisar():
  if (int(pegarValores()['feeds'][0]['field1']) < 50 or int(pegarValores()['feeds'][0]['field1']) > 120) (int(pegarValores()['feeds'][0]['field2']) < 70):
    
    print(pegarValores()['feeds'][0]['field1'])
    
    eu = 'o.9CYuBlpove3ErChfkLDjcmkNcjquJ1oz'
    danilo = 'o.I9Gpl2LNaKCSqRJ9PDo5buOcG9KQYgsi'

    usuarios = [eu, danilo]

    for usuario in usuarios:
      pbt = Pushbullet(usuario)
      pbt.push_note(
          '⚠️ALerta⚠️', f'O sistema【𝟭】 recebeu dados de risco\nBPM: {pegarValores()["feeds"][0]["field1"]} | SpO2: {pegarValores()["feeds"][0]["field2"]}')


while True:
  avisar()

  time.sleep(20)