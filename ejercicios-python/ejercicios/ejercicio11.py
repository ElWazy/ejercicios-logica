# Escribir un programa que pida al usuario un número entero positivo
# y muestre todos los números impares desde 1 hasta ese número.
print('\n## EJERCICIO 11 ##\n')

num1 = int(input('Ingrese un numero: '))

if num1 > 0:
    contador = 1
    while contador <= num1:
        if (num1 % 2) != 0:
            print(contador)
            contador += 2