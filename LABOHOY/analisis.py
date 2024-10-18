
# Importamos bibliotecas
import pandas as pd
from inline_sql import sql, sql_val
import numpy as np
import matplotlib.pyplot as plt # Para graficar series multiples
from   matplotlib import ticker   # Para agregar separador de miles
import seaborn as sns           # Para graficar histograma


miprefijo= "/home/Estudiante/Escritorio/LABOHOY/"

archivo_completo=  "TiemposReaccion.csv"
archivo_completo2=  "TiemposReaccion2.csv"

datos= pd.read_csv(miprefijo+archivo_completo)
datos2= pd.read_csv(miprefijo+archivo_completo2)

#%%
consultasql=sql^"""
SELECT Tiempo, CASE
                    WHEN Mano LIKE '%zq%' then 'izquierda'
                    ELSE 'derecha'
                    END AS Mano
FROM datos
"""



#%%


# Genera el grafico de frecuencias (mejorando la informacion mostrada)

plt.rcParams['font.family'] = 'sans-serif'           # Modifica el tipo de letra
plt.rcParams['axes.spines.right'] = False            # Elimina linea derecha  del recuadro
plt.rcParams['axes.spines.left']  = True             # Agrega  linea izquierda  del recuadro
plt.rcParams['axes.spines.top']   = False            # Elimina linea superior del recuadro

fig, ax = plt.subplots()

sns.histplot(data = consultasql,x="Tiempo", bins = 6,hue='Mano',palette ='colorblind',kde=True,stat='probability')

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes    
ax.set_title('Distribución de tiempo de reaccion de clicks')
ax.set_xlabel('Tiempo de reaccion (segundos)')
ax.set_ylabel('Cantidad de personas')

#%%

#%%


# Genera el grafico de frecuencias (mejorando la informacion mostrada)

plt.rcParams['font.family'] = 'sans-serif'           # Modifica el tipo de letra
plt.rcParams['axes.spines.right'] = False            # Elimina linea derecha  del recuadro
plt.rcParams['axes.spines.left']  = True             # Agrega  linea izquierda  del recuadro
plt.rcParams['axes.spines.top']   = False            # Elimina linea superior del recuadro

fig, axes =plt.subplots(1, 2, figsize=(12, 6))

sns.histplot(data = datos2,x="mano_no_habil", bins = 7,ax=axes[0],
             palette ='colorblind',kde=True,stat='probability')

sns.histplot(data = datos2,x="mano_habil", bins = 7,ax=axes[1],
             palette ='colorblind',kde=True,stat='probability',color='red')


axes[1].set_title('Distribución de tiempo de reaccion de clicks')
axes[1].set_xlabel('Tiempo de reaccion (segundos), MANO HABIL')
axes[1].set_ylabel('Frecuencia')
axes[1].set_xlim(0.5, 3)

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes    
axes[0].set_title('Distribución de tiempo de reaccion de clicks')
axes[0].set_xlabel('Tiempo de reaccion (segundos), MANO NO HABIL')
axes[0].set_ylabel('Frecuencia')
axes[0].set_xlim(0.5, 3.1)



