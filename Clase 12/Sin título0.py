#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
from inline_sql import sql, sql_val

"""
Created on Fri Oct  4 09:33:33 2024

@author: Estudiante
"""

datos= pd.read_excel("informacion-publica-dengue-zika-nacional-hasta-20201231_1(1).xlsx")

#%%

#OBJETIVO: VER Q TODOS LOS DATOS EVENTO_NOMBRE SON DEL MISMO TIPO

consultaSQL="""
SELECT evento_nombre
FROM datos
"""

eventos=sql^ consultaSQL

elejirString=sql^"""
SELECT COUNT(evento_nombre) as cantNoStrings
FROM eventos 
WHERE evento_nombre != 'Dengue' AND evento_nombre!='Zika'
"""

