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



prueba= especies(parques)

#print(prueba)

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

#print((leer_parque2(narchivo,parque))[112])




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

#print(alturas.agg("max"))



#muchas dudas


#5. Escribir una función obtener_inclinaciones(lista_arboles, especie)
#que, dada una lista como la generada con leer_parque(...) y una especie
#de árbol, devuelva una lista con las inclinaciones (columna 'inclinacio') de
#los ejemplares de esa especie.

def obtener_inclinaciones(lista_arboles, especie:str):

    inclinaciones = lista_arboles[lista_arboles["nombre_com"]==especie]

    inclinacionesEspecies = inclinaciones["inclinacio"]

    return inclinacionesEspecies



def especimen_mas_inclinado(lista_arboles  ):       #-->DF
    especie:list = especies(lista_arboles)

    especieMax= ""

    inclinacionMax = 0

    for i in range(len(especie)):
        incls = obtener_inclinaciones(lista_arboles,especie[i])
        inclinacionIterar=incls.agg("max")

        if inclinacionIterar > inclinacionMax:
            especieMax = especie[i]
            inclinacionMax = inclinacionIterar

    return [especieMax,inclinacionMax]


a = especimen_mas_inclinado(parques)

parqueCentenario = leer_parque(narchivo,"CENTENARIO")
losAndes = leer_parque(narchivo, "ANDES, LOS")

b = especimen_mas_inclinado(parqueCentenario)


"""
7. Volver a combinar las funciones anteriores para escribir la función
especie_promedio_mas_inclinada(lista_arboles) que, dada una lista
de árboles devuelva la especie que en promedio tiene la mayor inclinación y el
promedio calculado.
Resultados. Debería obtenerse, por ejemplo, que los Álamos Plateados del
Parque Los Andes tiene un promedio de inclinación de 25 grados
"""

def especie_promedio_mas_inclinad(lista_arboles):
    especie:list = especies(lista_arboles)

    inclinacionMaxProm:float= 0.0 

    especieMax= ""

    promedioMax:float = 0.0

    

    for i in range(len(especie)):
        incls = obtener_inclinaciones(lista_arboles,especie[i])
        inclinacionIterar=incls.agg("mean")

        if inclinacionIterar > inclinacionMaxProm:
            especieMax = especie[i]
            inclinacionMaxProm = inclinacionIterar

    return [especieMax,inclinacionMaxProm]

c = especie_promedio_mas_inclinad(losAndes)







#VAMOS A ARMAR UN DF

narchivo="arbolado-publico-lineal-2017-2018.csv"


dfVeredas= pd.read_csv(narchivo)

dfVeredasPosta = dfVeredas[["nombre_cientifico","ancho_acera","diametro_altura_pecho","altura_arbol"]]

especiesSeleccionadas=['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']


df = pd.read_csv("arbolado-en-espacios-verdes.csv", index_col = 2)

#print(df)

parquesJacaranda = df[["nombre_com"]]

#parquesJacaranda = df[df["nombre_com"]==('Jacarandá')]


pjr=parquesJacaranda.copy()

pjr.rename(columns={"altura_tot": "altura_arbol", "nombre_com": "nombre_cientifico","diametro":"diametro_altura_pecho"},inplace=True)

print(pjr.columns)

#ya esta el de los parques con las columnas cambiadas, resta comparar