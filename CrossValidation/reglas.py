import csv
from test import *
#from arbolKD import *

def escribir(ejemplo,resultado):
    print(ejemplo[0]," ",resultado, " acerto :", comparar(ejemplo,resultado))
    
    
def comparar(ejemplo,resultado):
    if(str(resultado)==ejemplo[17]):
        return True
    return False
    
def reescritura(ejemplos):
    contador = 0
    for ejemplo in ejemplos:
        resultado= evaluar(ejemplo)
        contador = contador+comparar(ejemplo,resultado)
        
        escribir(ejemplo,resultado)
        
    print("aciertos: ",contador,"Total datos: ",len(ejemplos)  )
    
    
    
def leer_fichero():
    lista=[]
    with open('parkinsons.data') as f:    
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            lista.append(row)
    return lista
    

cabecera = (leer_fichero()[0])
print("cabecera: ", cabecera ,"\nl")

ejemplos = leer_fichero()[1::]
reescritura(ejemplos)