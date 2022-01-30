import math


linea = input()   
# "1 1 -6"
arreglo =linea.split()
# arreglo[0] -> "1"
# arreglo[1] -> "1"
# arreglo[2] -> "-6"
A = arreglo[0]
# "1"
A = int(A)
# 1


B = arreglo[1]
B = int(B)

C = arreglo[2]
C = int(C)

raiz = B*B - 4*A*C
raiz = math.sqrt(raiz)

x1 = -B + raiz
x2 = -B - raiz 

x1 = x1/(2*A)
x2 = x2/(2*A)

print(str(x1) + ' ' + str(x2))