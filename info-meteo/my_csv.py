import csv
import numpy as np

#apre il file, mostra il nome delle colonne della tabella e il numero di righe del file
with open('rdu-weather-history.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')    #file
    line_count = 0

    #legge e stampa riga per riga, il nome delle colonne
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            columns = np.array([])
            columns = row
            line_count += 1
        else:
            line_count += 1
    #stampa il numero il numero di righe che compongono il file
    print(f'Processed {line_count} lines.')

with open('rdu-weather-history.csv') as csv_file:

    #input della data
    data = input("Inserisci il giorno gg/mm/aaaa: ") 
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    #legge riga per riga il file, finché non trova la data in input e la stampa
    for row in csv_reader:
        if line_count == 0:
            columns = np.array([])
            columns = row
            line_count += 1
        elif row[0] == data:
            print(f'{columns[0]}: {row[0]};\n{columns[1]}: {row[1]};\n{columns[2]}: {row[2]};')
            line_count += 1