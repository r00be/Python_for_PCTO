import requests   #permette di inviare richieste HTTP
import json       #permette di lavorare con i dati JSON

#inizializzazione delle variabili
city_code = ""
max_temp = 0.0
min_temp = 60.0
k = 0
somma = 0.0

#funzione che ritorna il valore della temperatura di una città
def request_temp(city_code):
  
  payload = {}
  headers = {}

  #legge il codice della città, affinché sia un numero intero
  try:
    response = requests.request("GET", URL, headers=headers, data=payload)
    dataJson = json.loads(response.text) # response.text ==> Json (tipo Dizionario)
    return dataJson["temperatura"] #restituisce la temperatura
  except:

    #se l'input è una stringa corrispondente a 'stop', si ferma
    if(city_code == "stop"): 
      print("\n")
      return None
    #altrimenti segnala errore
    else:
      print("ERRORE: '" + str(city_code) + "'qwer è una richiesta non accettata")

#inserimento del codice, affinché sia diverso da 'stop'
print("Inserisci codice-città da ricercare, 'stop' per terminare")
while city_code != "stop":  
  city_code = input("\n> ")
  URL = "https://meteo.corriere.it/meteoapi.php?c=" + str(city_code) #URL del corriere
  result = request_temp(city_code)
  
  #calcolo della Massima e Minima temperatura
  if(result != None):
    print(result)
    k += 1
    somma = somma + float(result)

    temp = float(result)
    if(temp > max_temp): max_temp = temp
    elif(temp < min_temp): min_temp = temp

#se il divisore è diverso da 0, calcola la media e stampa media, temperatura massima e minima
if(k != 0):
  media = float(somma/k)
  print("Temperatura media: ", media)
  print("Temperatura max: ", max_temp)
  print("Temperatura min: ", min_temp)