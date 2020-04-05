# Dados dos numeros reales. Indique cual es el mayor.
print('\n## EJERCICIO 2 ##\n')

num1 = float(input('ingrese un numero: '))
num2 = float(input('ingrese otro numero: '))

if num1 > num2:
    print(str(num1) + ', es mayor que ' + str(num2))
else:
    print(str(num2) + ', es mayor que ' + str(num1))