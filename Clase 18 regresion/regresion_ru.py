#%%
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn

#%%
# Importa el archivo como dataframe
data = pd.read_csv('/home/Estudiante/Escritorio/Clase 18 regresion/yacares.csv', sep=",")

#%%
data.head()

#%%
# Armamos un dataframe para cada variable
x = pd.DataFrame(data["RU"])
y = pd.DataFrame(data["DI"])

#%%
# Generamos una variable de tipo modelo lineal
model = linear_model.LinearRegression()
# Se ejecuta el algoritmo de fiteo a partir de las variables x e y
model.fit(x,y)

#%%
# Mostramos los valores de la pendiente y la intercept
print(model.coef_) #ESte es el b
print(model.intercept_) #Este es el a


#%%

# plot de la recta y de los puntos
plt.scatter(x, y,  color='black')
plt.plot(x, model.predict(x), color='blue', linewidth=3)
plt.xlabel("Dosis de RU (ug/huevo)")
plt.ylabel("Indice de daño")
plt.show()

#%%
print(model.score(x, y))

#%%
#Otra manera de hacer el modelo
# Agregar una constante para el término de intercepto
x_const = sm.add_constant(x)

# Crear el modelo con statsmodels
model = sm.OLS(y, x_const)
results = model.fit()

# Resumen completo
print(results.summary())
#%%
#EJERCICIO EN CLASE:

muestra = pd.read_csv("/home/Estudiante/Escritorio/Clase 18 regresion/datos_libreta_15122003.csv")

#scatter

plt.scatter(x=muestra['RU'],y=muestra['ID'])
plt.xlabel("Dosis de RU (ug/huevo)")
plt.ylabel("Indice de daño")
plt.show()


#%%

x=muestra[['RU']]
y=muestra[['ID']]

model = linear_model.LinearRegression()
# Se ejecuta el algoritmo de fiteo a partir de las variables x e y
model.fit(x,y)

plt.plot(x, model.predict(x), color='red', linewidth=3)
#%%

b=model.coef_ #ESte es el b
a=model.intercept_ #Este es el a

print(f'la ecuacion es F(x) = {a} + x{b}')

R=model.score(x, y)
print(R)
#%%
coeficientes= pd.read_csv('/home/Estudiante/Escritorio/Clase 18 regresion/resultado.csv')



seaborn.histplot(data=coeficientes,bins=6,palette='colorblind')










