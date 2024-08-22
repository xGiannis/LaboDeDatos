import pandas as pd
import numpy as np

narchivo="arbolado-en-espacios-verdes.csv"

parque= "GENERAL PAZ"


def leer_parque(narchivo:str,parque:str):


    df = pd.read_csv(narchivo, index_col = 2)

    res= df[df["espacio_ve"]==parque]


    return res



parques = leer_parque(narchivo,parque)

df = pd.read_csv(narchivo, index_col = 2)

def especies(lista_arboles) -> list:        #lista arboles es un csv
    

    listaEspecies=[]
    especies=(lista_arboles["nombre_com"]).drop_duplicates()



    #print(especies)
    for e in especies:
        listaEspecies.append(e)

    #print(listaEspecies)


    return listaEspecies



especie= especies(parques)

#print(parques.shape[0])




def contar_ejemplares(lista_arboles) -> list:

    especies=(lista_arboles["nombre_com"])

    repeticiones:dict[str,int] = {}



    for i in especies:
        if i in repeticiones:
            repeticiones[i] = repeticiones[i] + 1
        else:
            repeticiones[i] = 1
        pass

    return repeticiones
    
ejemplares= contar_ejemplares(parques)

def contar_ejemplares2(lista_arboles) -> list:

    res = lista_arboles["nombre_com"].value_counts(dropna = False)
    return res
    


#print(ejemplares)
    





###########ME PARECE Q LO HICE MAL, EL PRIMER EJERCICIO NO DEVUELVE UNA LISTA DE DICCIONARIOS, SI NO UN DATAFRAME


def leer_parque2(narchivo:str,parque:str):


    df = pd.read_csv(narchivo, index_col = 2)



    res= df[df["espacio_ve"]==parque]

    listaDic = []


    for i in range(len(res)):
        fila = res.iloc[i]
        dic = fila.to_dict()
        listaDic.append(dic)
    


    return listaDic

print((leer_parque2(narchivo,parque))[112])




#######ESTO ES SI ES QUE HUBIERE DEVOLVERE LISTERE.


#continuo como vnia antes.

columna = "altura_tot"

def obtener_alturas(lista_arboles, especie):
    especies=(lista_arboles[lista_arboles["nombre_com"]==especie])

    #aca tengo el df pero solo con la especie seleccionada

    alturasEspecies = especies[columna]

    return alturasEspecies


alturas=obtener_alturas(parques,"Jacarandá")

#print(alturas)

print(alturas.agg("max"))



#muchas dudas


#5. Escribir una función obtener_inclinaciones(lista_arboles, especie)
#que, dada una lista como la generada con leer_parque(...) y una especie
#de árbol, devuelva una lista con las inclinaciones (columna 'inclinacio') de
#los ejemplares de esa especie.

def obtener_inclinaciones(lista_arboles, especie):

    inclinaciones = lista_arboles[lista_arboles["nombre_com"]==especie]

    inclinacionesEspecies = inclinaciones["inclinacio"]

    return inclinacionesEspecies



def especimen_mas_inclinado(lista_arboles):
    especies = especie(lista_arboles)

    inclinacionMax= []

    especieMax= ""

    inclinacionMax = 0

    for i in range(len(especies)):
        incls = obtener_inclinaciones(lista_arboles,especies)
        inclinacionIterar=incls.agg("max")

        if inclinacionIterar > inclinacionMax:
            especieMax == especies[i]

    return [especieMax,inclinacionMax]
        



