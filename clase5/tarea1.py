def matrizEmpleado1():

    empleado1=[20222,45,2,20]

    empleado2=[33456,40,0,25]

    empleado3=[45423,42,1,10]

    res = [empleado1,empleado2,empleado3]

    return res



#print(matrizEmpleado1())

empleados=matrizEmpleado1()



def superanSalarioActividad01(empleado01,umbral):
    
    res = []

    for i in range(len(empleado01)):
        if empleado01[i][3] >= umbral:
            res.append(empleado01[i])

    return res


empleadosQsuperan = superanSalarioActividad01(empleados,11)

#print(empleadosQsuperan)


empleado4 = [43967,37,0,12]
empleado5 = [42236276,36,0,18]

empleados.append(empleado4)
empleados.append(empleado5)

empleadosQsuperan2 = superanSalarioActividad01(empleados,11)

#print(empleadosQsuperan2)

empleados_2=[[20222333,20,45,2],[33456234,25,40,0],[45432345,10,41,1],[43967305,12,37,0],[42236276,18,36,0]]

def superanSlarioActividad03(empleados,umbral):

    for i in range(len(empleados_2)):

        salario=empleados[i][1]
        edad=empleados[i][2]
        hijos=empleados[i][3]

        empleados[i][1]=edad
        empleados[i][2]=hijos
        empleados[i][3]=salario

    return superanSalarioActividad01(empleados,umbral)
    

#print(superanSlarioActividad03(empleados_2,11))


empleadosColumnas=[[20222333,33456234,45432345,43967305,42236276],[20,25,10,12,18],[45,40,41,37,36],[2,0,1,0,0]]


def superanSalarioActividad05(empleados,umbral):
    filasNomrmal=[]
    for i in range(len(empleados[0])):
        empleado=[]
        for j in range(len(empleados)):
            empleado.append(empleados[j][i])
        
        
        filasNomrmal.append(empleado)


    return superanSlarioActividad03(filasNomrmal,umbral)

        

print(superanSalarioActividad05(empleadosColumnas,11))