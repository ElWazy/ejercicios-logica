# Dado un numero entero, indique si este es par o no.
print('\n## EJERCICIO 1 ##\n')

num1 = int(input('ingrese un numero: '))

if (num1 % 2) == 0:
    print(str(num1) + ', es par.')
else:
    print(str(num1) + ', es impar')