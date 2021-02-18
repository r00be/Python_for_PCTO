import pandas as pd     #Ha funzioni per analizzare, pulire, esplorare e manipolare i dati.

df = pd.read_csv("anagrafica-vaccini.csv")

print(df.info())

men = df["sesso_maschile"]    #filtro i dati relativi alla colonna "sesso_maschile"
print("\nSesso Maschile")
print(men)                      #stampo le informazioni relative a questa serie

#sommando tutti i valori in questa serie ottengo il numero totale vaccini somministrati a uomini
cont = 0
for x in men:
    cont += x
print("Numero Vaccini somministrati a uomini:", cont)


#Esempio 2: seleziono i dati provenienti da piu' colonne - ottengo un nuovo data frame
#seleziono i dati di due colonne - equivale a una proiezione su due colonne
#sono i vaccini somministrati a uomini suddivisi per fascia anagrafica

df_m = df[["fascia_anagrafica", "sesso_maschile"]]
print("\nVaccini somministrati a uomini suddivisi per fascia anagrafica")
print(df_m)

#Voglio calcolare il numero di vaccini somministrati a uomini tra 16 e 39 anni
#df_m.values restituisce l'insieme dei valori di df_m 
#sono delle coppie di valori: fascia anagrafica - numero vaccini effettuati
cont = 0 
for (fascia, n) in df_m.values:
    if fascia == "16-19" or fascia =="20-29" or fascia == "30-39":
        cont += n
print("\nNumero Vaccini somministrati a uomini tra 16 e 39 anni:", cont)



'''
-----------------------------------------------------------------------------------------
Provate a determinare il numero di operatori sanitari e socio-sanitari che hanno ricevuto
entrambe le dosi di vaccino.

Determinare il numero di donne che hanno ricevuto la prima dose di vaccino
-----------------------------------------------------------------------------------------
'''


#calcola il numero delle seconde dosi di vaccini somministrati a operatori sanitari e sociosanitari
operatori = df[["categoria_operatori_sanitari_sociosanitari", "totale"]]
cont = 0
cont_tot = 0
for(x,y) in operatori.values:
    cont += x
    cont_tot += y
print("\n\nNumero operatori = ", cont)
print("Numero totale = ", cont_tot)

sec_dose = df["seconda_dose"]
cont_dos = 0
for x in sec_dose:
    cont_dos += x
print("Numero totale di seconde dosi: ", cont_dos)

#calcola la proporzione tra i vaccini della seconda dose degli operatori, rispetto ai vaccini totali
num_dosi = int((cont_dos*cont)/(cont_tot))
print("Vaccini somministrati a operatori sanitari e sociosanitari: ", num_dosi)

#calcola il numero delle prime dosi di vaccini somministrati a donne
women_fd = df[["sesso_femminile", "prima_dose"]]
cont = 0
cont_fd = 0
for (x,y) in women_fd.values:
    cont += x
    cont_fd += y

#calcola la proporzione tra i vaccini della prima dose delle donne, rispetto ai vaccini totali
women_fd = int((cont_fd*cont)/(cont_tot))
print("Vaccini somministrati donne della prima dose: ", women_fd)

