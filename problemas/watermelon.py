linea = input()
peso = int(linea)

if (peso < 3):
    print("NO")

else:
    hola = peso%2
    if (hola == 1):
        print ("NO")
    else:
        print ("SI")