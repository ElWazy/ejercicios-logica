# Desde un dispositivo de E/S se leen tres numeros. Indique cual es el mayor.
print('\n## EJERCICIO 3 ##\n')

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
num3 = int(input('Ingrese otro numero mas: '))

if num1 == num2 and num2 == num3:
    print('Son todos los numeros iguales')

elif num1 > num2 and num1 > num3:
    print(str(num1) + ', es mayor que ' + str(num2) + " y " + str(num3))

elif num2 > num1 and num2 > num3:
    print(str(num2) + ', es mayor que ' + str(num1) + " y " + str(num3))

elif num3 > num2 and num3 > num1:
    print(str(num3) + ', es mayor que ' + str(num2) + " y " + str(num1))