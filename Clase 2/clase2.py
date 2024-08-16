#vamos a leer el archivo de la clase 2. Podemos buscar el path si no esta en la carpeta. DESCARGAS/DATAME.TXT

#CON ../ SUBO ARRIBA UNA DIRECCION - OSEA YO DE ACA QUEDARIA EN LA CARPETA DEL GIT ORIGINAL. 

#Si no, con ~ paso la direccion desde el root.

#nombre_archivo

f=open("datame.txt","rt")

data=f.read()

print(data)

f.close()