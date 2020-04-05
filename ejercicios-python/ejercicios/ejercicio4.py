# Crear programa en el que se almacenen 3 números en 3 variables (las que usted quiera).
# El programa debe decidir cuál es el mayor y es el menor de los 3.
print('\n## EJERCICIO 4 ##\n')

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
num3 = int(input('Ingrese un numero mas: '))

numMayor = 0
numMenor = 0

if num1 == num2 and num2 == num3:
    print('Son todos los numeros iguales')

elif num1 > num2 and num1 > num3:
    numMayor = num1

    if num2 > num3:
        numMenor = num3

        print(str(numMayor) + ', es el numero mayor.')
        print(str(numMenor) + ', es el numero menor.')
    else:
        numMenor = num2

        print(str(numMayor) + ', es el numero mayor.')
        print(str(numMenor) + ', es el numero menor.')

elif num2 > num1 and num2 > num3:
    numMayor = num2

    if num1 > num3:
        numMenor = num3

        print(str(numMayor) + ', es el numero mayor.')
        print(str(numMenor) + ', es el numero menor.')
    else:
        numMenor = num1

        print(str(numMayor) + ', es el numero mayor.')
        print(str(numMenor) + ', es el numero menor.')

elif num3 > num1 and num3 > num2:
    numMayor = num3

    if num1 > num2:
        numMenor = num2

        print(str(numMayor) + ', es el numero mayor.')
        print(str(numMenor) + ', es el numero menor.')
    else:
        numMenor = num1

        print(str(numMayor) + ', es el numero mayor.')
        print(str(numMenor) + ', es el numero menor.')