import pandas as pd


nombre = "Clase-03-Actividad-01-Datos.csv"


datos = pd.read_csv(nombre)

print(datos)

movilidad = pd.read_csv("Encuesta de Movilidad - Respuestas de formulario 1.csv")


res=movilidad["Tipo de transporte utilizado"].value_counts(dropna=False)