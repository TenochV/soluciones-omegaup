linea = input()
pesoTotal = int(linea)

resultado = False
peso1 = 1
while(peso1 < pesoTotal):
    peso2 = pesoTotal - peso1

    sobrante1 = peso1%2
    sobrante2 = peso2%2
    
    esPar1 = sobrante1 == 0
    espar2 = sobrante2 == 0

    if (esPar1 and espar2):
        resultado = True
        break
    peso1 = peso1 + 1

if (resultado):
    print("Si")
else:
    print("No")