
"""
Created on Tue Sep 10 14:31:17 2024

@author: Estudiante
"""
# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase.
Autor  : Pablo Turjanski
Fecha  : 2024-03-25
"""
#%%===========================================================================
# Importamos bibliotecas
import pandas as pd
import numpy as np
from inline_sql import sql, sql_val


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

#carpeta = "C:/Users/usuario/Desktop/LaboDeDatos/guia_practica_SQL/Guía Práctica - SQL - Archivos adjuntos-20240910/"

carpeta = "~/Escritorio/LABO/LaboDeDatos/guia_practica_SQL/Guía Práctica - SQL - Archivos adjuntos-20240910/"


# Ejercicios AR-PROJECT, SELECT, RENAME
casos       = pd.read_csv(carpeta+"casos.csv")
grupoetario      = pd.read_csv(carpeta+"grupoetario.csv")
tipoevento   = pd.read_csv(carpeta+"tipoevento.csv")
provincia        = pd.read_csv(carpeta+"provincia.csv")
departamento = pd.read_csv(carpeta+"departamento.csv")

#A. Consultas sobre una tabla

"""a. Listar sólo los nombres de todos los departamentos que hay en la tabla
departamento (dejando los registros repetidos)."""


consultaSQL = """
SELECT descripcion,
FROM departamento
              """

dataframeResultado = sql^ consultaSQL




"""b. Listar sólo los nombres de todos los departamentos que hay en la tabla
departamento (eliminando los registros repetidos)."""




consultaSQL = """
SELECT DISTINCT descripcion,
FROM departamento
              """

dataframeResultado = sql^ consultaSQL


"""c. Listar sólo los códigos de departamento y sus nombres, de todos los
departamentos que hay en la tabla departamento."""





consultaSQL = """
SELECT DISTINCT descripcion, id
FROM departamento
              """

dataframeResultado = sql^ consultaSQL


"""d. Listar todas las columnas de la tabla departamento."""


consultaSQL = """
SELECT *
FROM departamento
              """

dataframeResultado = sql^ consultaSQL

dataframeResultado = dataframeResultado.columns


"""e. Listar los códigos de departamento y nombres de todos los departamentos
que hay en la tabla departamento. Utilizar los siguientes alias para las
columnas: codigo_depto y nombre_depto, respectivamente."""


consultaSQL = """
SELECT id AS codigo_depto, descripcion AS nombre_depto
FROM departamento
              """

dataframeResultado = sql^ consultaSQL



"""f. Listar los registros de la tabla departamento cuyo código de provincia es
igual a 54"""


consultaSQL = """
SELECT *
FROM departamento
WHERE id_provincia=54
              """

dataframeResultado = sql^ consultaSQL





"""g. Listar los registros de la tabla departamento cuyo código de provincia es
igual a 22, 78 u 86."""


consultaSQL = """
SELECT *
FROM departamento
WHERE id_provincia=54 OR id_provincia=78 OR id_provincia=86
              """

dataframeResultado = sql^ consultaSQL



"""h. Listar los registros de la tabla departamento cuyos códigos de provincia se
encuentren entre el 50 y el 59 (ambos valores inclusive)."""


consultaSQL = """
SELECT *
FROM departamento
WHERE 50<= id_provincia AND id_provincia <= 59
              """

dataframeResultado = sql^ consultaSQL


#B. Consultas multitabla (INNER JOIN)

"""a. Devolver una lista con los código y nombres de departamentos, asociados al
nombre de la provincia al que pertenecen."""


consultaSQL = """
SELECT d.id, d.descripcion , provincia.descripcion
FROM departamento as d
INNER JOIN provincia
ON d.id_provincia = provincia.id
              """

dataframeResultado = sql^ consultaSQL


#el b es igual???


"""c. Devolver los casos registrados en la provincia de “Chaco”."""

depasChaco = sql^"""
SELECT d.id
FROM departamento as d
INNER JOIN provincia AS p
ON d.id_provincia = p.id
WHERE p.descripcion = 'Chaco'
              """
#estos son los depas de chaco


consultaSQL = """
SELECT *
FROM casos as c
INNER JOIN depasChaco
ON c.id_depto = depasChaco.id
              """


dataframeResultado = sql^ consultaSQL


"""d. Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo
cantidad supere los 10 casos."""




depasChaco = sql^"""
SELECT d.id
FROM departamento as d
INNER JOIN provincia AS p
ON d.id_provincia = p.id
WHERE p.descripcion = 'Buenos Aires'
              """
#estos son los depas de chaco


consultaSQL = """
SELECT *
FROM casos as c
INNER JOIN depasChaco
ON c.id_depto = depasChaco.id
WHERE c.cantidad > 10
              """

dataframeResultado = sql^ consultaSQL


#C. Consultas multitabla (OUTER JOIN)


"""a. Devolver un listado con los nombres de los departamentos que no tienen
ningún caso asociado."""

consultaSQL = """
SELECT DISTINCT d.descripcion
FROM departamento AS d
LEFT OUTER JOIN casos AS c
ON d.id = c.id_depto
WHERE c.cantidad = NULL
              """

dataframeResultado = sql^ consultaSQL
#todos los casos estan asociados, perdi tiempo de mi vida con esta pija

"""b. Devolver un listado con los tipos de evento que no tienen ningún caso
asociado.
"""
consultaSQL = """
SELECT DISTINCT descripcion
FROM tipoevento AS t
LEFT OUTER JOIN casos AS c
ON t.id = c.id_tipoevento
WHERE anio IS NULL
              """


dataframeResultado = sql^ consultaSQL


#D. Consultas resumen

"""a)Calcular la cantidad total de casos que hay en la tabla casos.
"""


consultaSQL = """
SELECT SUM(cantidad) as CASOSTOTALES
FROM casos
              """

dataframeResultado = sql^ consultaSQL



"""b. Calcular la cantidad total de casos que hay en la tabla casos para cada año y
cada tipo de caso. Presentar la información de la siguiente manera:
descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso
(ascendente) y año (ascendente).
"""


consultaSQL = """
SELECT SUM(c.cantidad) as CASOSTOTALES, c.anio,c.id_tipoevento,t.descripcion
FROM casos as c
INNER JOIN tipoevento as t
ON c.id_tipoevento = t.id
GROUP BY c.anio , c.id_tipoevento, t.descripcion
ORDER BY id_tipoevento ASC, anio ASC

              """

dataframeResultado = sql^ consultaSQL


"""c. Misma consulta que el ítem anterior, pero sólo para el año 2019.

"""


consultaSQL = """
SELECT SUM(c.cantidad) as CASOSTOTALES, c.anio,c.id_tipoevento,t.descripcion
FROM casos as c
INNER JOIN tipoevento as t
ON c.id_tipoevento = t.id
WHERE c.anio = 2019
GROUP BY c.anio , c.id_tipoevento, t.descripcion
ORDER BY id_tipoevento ASC, anio ASC
              """

dataframeResultado = sql^ consultaSQL


"""d. Calcular la cantidad total de departamentos que hay por provincia. Presentar
la información ordenada por código de provincia.
"""


depasTotalesPorProvincia = sql ^ """
SELECT COUNT(*) as depasPorProvincia, id_provincia, p.descripcion
FROM departamento
INNER JOIN provincia as p
ON id_provincia = p.id
GROUP BY id_provincia, p.descripcion


"""

#consultaSQL = 
"""
SELECT p.id
FROM provincia as p
INNER JOIN tipoevento as t
ON c.id_tipoevento = t.id
GROUP BY p.id
ORDER BY p.id
              """

dataframeResultado = sql^ consultaSQL






"""e. Listar los departamentos con menos cantidad de casos en el año 2019.

"""


consultaSQL = """
SELECT DISTINCT d.descripcion, SUM(c.cantidad) as casosPorDepa, d.id
FROM departamento as d
INNER JOIN casos as c
ON c.id_depto = d.id
WHERE c.anio = 2019 
GROUP BY d.descripcion, d.id
ORDER BY casosPorDepa ASC
LIMIT 10
              """
              

dataframeResultado = sql^ consultaSQL


"""f. Listar los departamentos con más cantidad de casos en el año 2020.
"""



consultaSQL = """
SELECT d.descripcion, SUM(c.cantidad) as casosPorDepa, d.id,d.id_provincia
FROM departamento as d
INNER JOIN casos as c
ON c.id_depto = d.id
WHERE c.anio = 2020
GROUP BY  d.id, d.id_provincia, d.descripcion
ORDER BY casosPorDepa DESC
LIMIT 15
              """

#los resultados son logicos (no racism). Es dengue, no covid, tiene sentido q el norte este foerte

dataframeResultado = sql^ consultaSQL


"""g. Listar el promedio de cantidad de casos por provincia y año.

"""

casosAño = consultaSQL = sql^"""
SELECT DISTINCT d.descripcion, SUM(c.cantidad) as casosPorDepa, d.id,d.id_provincia,c.anio
FROM departamento as d
INNER JOIN casos as c
ON c.id_depto = d.id
GROUP BY  d.id, d.id_provincia, d.descripcion,c.anio
ORDER BY c.anio DESC,casosPorDepa DESC
              """




consultaSQL = """
SELECT AVG(c.casosPorDepa) as promedio_anio, c.anio, p.descripcion
FROM casosAño as c
INNER JOIN provincia as p
ON c.id_provincia = p.id
GROUP BY c.anio, p.descripcion 
ORDER BY c.anio DESC

              """


dataframeResultado = sql^ consultaSQL

"""h. Listar, para cada provincia y año, cuáles fueron los departamentos que más
cantidad de casos tuvieron"""

#podria hacer un limit 24 pero seria medio de cagon

maxCasosPorProvincia = sql^"""
SELECT MAX(casosPorDepa) as casosMax, id_provincia, anio, p.descripcion as provincia
FROM casosAño
INNER JOIN provincia as p
ON p.id = id_provincia
GROUP BY p.descripcion, anio,id_provincia

              """
              
casosPorProvincia = sql^"""
SELECT casosPorDepa as casos, id_provincia, anio, p.descripcion as provincia, casosAño.id, casosAño.descripcion as depa
FROM casosAño
INNER JOIN provincia as p
ON p.id = id_provincia
GROUP BY p.descripcion, anio,id_provincia, casosPorDepa, casosAño.id, depa
"""



consultaSQL = """
SELECT DISTINCT casosMax, mp.provincia, mp.anio, depa
FROM casosPorProvincia as cp
INNER JOIN maxCasosPorProvincia as mp
ON cp.id_provincia = mp.id_provincia AND casosMax = casos AND cp.anio = mp.anio 
GROUP BY mp.provincia, mp.anio, casosMax, depa
ORDER BY mp.anio DESC
              """

         
              
#yendo a dormir sin haberlo resuelto

dataframeResultado = sql^ consultaSQL

"""i. Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo la
provincia de Buenos Aires en el año 2019.
"""

casosBsas = sql^"""
SELECT cantidad, id_depto, anio, id_provincia
FROM casos
INNER JOIN departamento
ON id_depto = departamento.id
WHERE anio = 2019 and id_provincia = 6

"""


#####asumi q se el id, si no es hacer un inner join con prov y meterle q la descripcion sea buenos aires


########
consultaSQL = """
SELECT DISTINCT SUM(cantidad),MAX(cantidad), MIN(cantidad), AVG(cantidad)
FROM casosBsas
              """

dataframeResultado = sql^ consultaSQL



"""j. Misma consulta que el ítem anterior, pero sólo para aquellos casos en que la
cantidad total es mayor a 1000 casos.
"""

depasPorProv=sql^"""
SELECT DISTINCT d.id, d.descripcion as depa, d.id_provincia, p.descripcion as prov, (cantidad), anio, c.id
FROM departamento as d
INNER JOIN provincia as p
ON p.id = id_provincia
INNER JOIN casos as c
ON c.id_depto=d.id
ORDER BY id_provincia

"""



casosPorProv1000=sql^"""
SELECT SUM(cantidad) as cantProv, id_provincia, prov
FROM depasPorProv
GROUP BY id_provincia, prov
HAVING cantProv > 1000

"""



consultaSQL = """
SELECT DISTINCT SUM(cantidad),MAX(cantidad), MIN(cantidad), AVG(cantidad), prov
FROM depasPorProv
GROUP BY id_provincia, prov
HAVING SUM(cantidad) >(
       SELECT SUM(cantidad) as cantProv
       FROM depasPorProv
       GROUP BY id_provincia
       HAVING cantProv > 1000
)
              """
              
              #LE FALATAN CORDOBA Y CORRIENTES
              #WTF, CADA VEZ Q LO CORRO DA ALGO DIFERENTE
              #preguntar!!!!!!
              #puede ser q sea porque no especifico año

ALGODIF = sql^ consultaSQL


consultaSQL2 =sql^"""
SELECT DISTINCT SUM(dp.cantidad),MAX(dp.cantidad), MIN(dp.cantidad), AVG(dp.cantidad), d.prov
FROM casosPorProv1000 as d
INNER JOIN depasPorProv as dp
ON d.prov = dp.prov
WHERE dp.anio = 2019
GROUP BY d.prov

"""

#esta creo q da bien






