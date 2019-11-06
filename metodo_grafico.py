import matplotlib.pyplot as plt
import numpy as np

matriz = np.array([[1,2,120],[1,1,90]])
contribuciones = np.array([50,80])

#Defincion de restricciones
print('Estas son las restricciones del problema')
restriccion1 = str(matriz[0][0])+'x1' + '  ' + str(matriz[0][1] )+'X2'+ '  ' + '<='+str(matriz[0][2])
restriccion2 = str(matriz[1][0])+'x1' + '  ' + str(matriz[1][1] )+'X2'+ '  ' + '<='+str(matriz[1][2])
print(restriccion1)
print(restriccion2)

"""
Seccion de codigo para igualar una de las variables de las restricciones a 0 y concer el valor de X1 y X2 para cada unda de ellas
"""
puntos = []

filas = matriz.shape[0]
columnas = matriz.shape[1]
print('El arreglo tiene unas dimensiones de filas', str(filas) + ' y  '+ str(columnas)+' columnas' )

#removiendo la columna del costo
columnas_sin_resultado = columnas -1

for f in range(filas):
    #print('Fila',f)

    for c in range(columnas_sin_resultado):
        #print('Columna',c)

        v1 = matriz[f][c]
        v2 = matriz[f][-1]
        result = v2/v1
       # print("Igualando X", str(c+1) + ' a 0'+ str(result))
        #print(result)
        if c ==0:
            puntos.append([result,0])
        else:
            puntos.append([0,result])

print("Puntos a graficar ")
for a in puntos:
    print(a)

"""
Graficación de los puntos anteriores
"""
contador = len(puntos)
X = []
for b in range(4):
    X.append(puntos[b][0])
Y = []
for b in range(4):
    Y.append(puntos[b][1])


for a in range(0,contador):
    y = int(puntos[a][0])
    x = int(puntos[a][1])
    plt.plot(X,Y,'ro')

def connectpoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

connectpoints(X,Y,0,1)
connectpoints(X,Y,2,3)
plt.axis('equal')
plt.show()

"""

"""