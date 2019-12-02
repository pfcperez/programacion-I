import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString
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
    #print(x1,x2)
    #print(p1,p2)
    #idx = np.argwhere(np.diff(np.sign(x2-y2))).flatten()

    plt.plot([x1,x2],[y1,y2],'k-')
    return x1,x2,y1,y2


x1,x2,y1,y2 = connectpoints(X,Y,0,1)
x3,x4,y3,y4 = connectpoints(X,Y,2,3)
plt.axis('equal')
print("Puntos que se juntan ")
print(x1,x2)
print(x3,x4)
print("Puntos que se juntan ")
print(y1,y2)
print(y3,y4)
#idx = np.argwhere(np.diff(np.sign(x2-y2))).flatten()
line1 = LineString([(x1,x2),(x3,x4)])
line2 = LineString([(y1,y2),(y3,y4)])
intersection = line1.intersection(line2)
print(line1.length)

plt.show()

"""
respuesta correcta
X = 60
Y 29 o 30
https://www.science-emergence.com/Articles/How-to-write-a-simple-python-code-to-find-the-intersection-point-between-two-straight-lines-/
https://rosettacode.org/wiki/Find_the_intersection_of_two_lines#Python
https://shapely.readthedocs.io/en/stable/manual.html#linestrings

"""