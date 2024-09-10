#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from inline_sql import sql, sql_val


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

carpeta = "~/Escritorio/guia_practica_SQL/Guía Práctica - SQL - Archivos adjuntos-20240910/"


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

depas= sql^"""
SELECT d.id
FROM departamento as d
INNER JOIN provincia AS p
ON d.id_provincia = p.id
              """

consultaSQL = """
SELECT *
FROM casos as c
INNER JOIN depas
ON c.id_depto = depas.id
WHERE c.cantidad = 0
              """


dataframeResultado = sql^ consultaSQL



    
