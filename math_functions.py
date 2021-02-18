#Librerie
import numpy as np              #permette di lavorare con vettori, matrici e operazioni algebriche
import random as rnd            #modulo di numpy, permette di lavorare con numeri casuali
import matplotlib.pyplot as plt #utili per la visualizzazione di grafici


#Creazione di un array con le coordinate x
n=100
x = np.linspace(-(2*np.pi), 2*np.pi, n) #Restituisce n campioni equidistanti, presi nell'intervallo [-2π , 2π].

#Visualizzazione dei grafici
f1 = np.sin(x)
plt.plot(x, f1, color = 'red') 
plt.title("f(x)=sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

f2 = np.cos(x)
plt.plot(x, f2, color = 'red') 
plt.title("f(x)=cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

f3 = np.tan(x)
plt.plot(x, f3, color = 'red')
plt.title("f(x)=tan(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

f4 = np.exp(x)
plt.plot(x, f4, color = 'red')
plt.title("f(x)=e^x(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

f5 = np.log(x)
plt.plot(x, f5, color = 'red')
plt.title("f(x)=ln(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()