import pandas as pd                 #permette di elaborare analisi di dati
import matplotlib.pyplot as plt

#il file "movies.csv" viene assegnato alla variabile "lista", un DataFrame contenente righe e colonne del file
lista = pd.read_csv("movies.csv")   
lista.head()    
print(lista)


#assegna e stampa la variabile con i valori presenti nella colonna "Genre" e "Year"
genere_anno_incassi = lista[["Genre", "Year"]]
print(genere_anno_incassi)


#elaborazione incassi
tmp = lista["Worldwide Gross"] #variabile di appoggio contenente gli incassi

#converte le stringhe in valori float rimuovendo il simbolo "$" 
incassi = []
for i in tmp:
    incassi.append(float(i[1:]))

lista["Worldwide Gross"] = incassi

#produce un grafico dei valori e lo mostra
lista["Worldwide Gross"].plot() 
plt.show()