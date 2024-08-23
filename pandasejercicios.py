#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:16:23 2024

@author: Estudiante
"""
import pandas as pd

#Armar un dataframe que contenga las filas de Jacarandás y otro con los
#Palos Borrachos.

narchivo = "arbolado-en-espacios-verdes.csv"



df = pd.read_csv(narchivo, index_col=2)


jacarandas = df[df["nombre_com"]=="Jacarandá"]


paloBorracho = df[df["nombre_com"].str.startswith("Palo")]

cantmax=0


altmax=jacarandas["altura_tot"].agg("max")




def cantidad_arboles(parque):
    
    jacar = jacarandas[jacarandas["espacio_ve"]==parque]
    print(jacar)
    
    return len(jacar)

