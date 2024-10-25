#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Para graficar series multiples
from   matplotlib import ticker   # Para agregar separador de miles
import seaborn as sns 
from inline_sql import sql, sql_val
"""
Created on Fri Oct 25 11:00:39 2024

@author: Estudiante
"""
competencia= 'titanic_competencia.csv'
carpeta = "~/Escritorio/CATEGORIZACION/Clase 15 - archivos-20241025/"
fileTitanic = "titanic_training.csv"

titanicTraining = pd.read_csv(carpeta+fileTitanic)
titanicCompe = pd.read_csv(carpeta+competencia)

sobrevivientes=sql^"""
SELECT Pclass, Sex, Age
FROM titanicTraining
WHERE Survived == 1
ORDER BY Sex
"""

cantidadNinios = sql^"""
SELECT COUNT(Age)
FROM titanicTraining
WHERE Age <= 18
"""

cantidadMujeres=sql^"""
SELECT COUNT(Sex),Sex
FROM titanicTraining
GROUP BY Sex

"""

proporcionMujeres=sql^"""
SELECT COUNT(Sex),Sex
FROM titanicTraining
WHERE Survived == 1
GROUP BY Sex

"""




porporcionMujeresCLase1=sql^"""
SElECT COUNT(Sex),Sex,Pclass
FROM titanicTraining
WHERE Pclass == 1 
GROUP BY Sex,Pclass
"""
porporcionMujeresCLase122=sql^"""
SElECT COUNT(Sex),Sex,Pclass
FROM titanicTraining
WHERE Pclass == 1 AND Survived
GROUP BY Sex,Pclass
"""

porporcionTotalSobreiviente=sql^"""
SElECT COUNT(Pclass),Pclass
FROM titanicTraining
WHERE Survived == 1 AND Sex = 'female'
GROUP BY Pclass
"""

porporcionTotalMuertos=sql^"""
SElECT COUNT(Pclass),Pclass
FROM titanicTraining
WHERE Sex= 'female'
GROUP BY Pclass
"""






#%%






#%%




def clasificador_titanic(x):
    vive= False
    if x.Sex == 'female' and x.Pclass < 3:
        vive = True
    elif x.Sex == 'female' and x.Pclass == 3 and x.Age>50:
        vive=True
    elif x.Sex =="male" and x.Pclass == 1 and x.Age<18:
        vive=True
    elif x.Sex =="female" and x.Pclass == 3 and x.Age<18:
        vive=True
    return vive
        
    
for i in range(0,10):
    print(clasificador_titanic(titanicCompe.iloc[i]))
        
    
    
    
    
    
    
    
    


