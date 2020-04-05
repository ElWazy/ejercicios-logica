# Ingresar un numero por teclado e indique si está en el rango entre [5 y 9]
print('\n## EJERCICIO 7 ##\n')

num1 = int(input('Ingresar un numero: '))

if num1 >= 5 and num1 <= 9:
    print(str(num1) + ', se encuentra dentro de el 5 y el 9.')
else:
    print(str(num1) + ', no se encuentra entre de el 5 y el 9.')