# Desde una computadora se leen tres números.
# Indique cuál de ellos es la suma de los otros dos
print('\n## EJERCICIO 9 ##\n')

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
num3 = int(input('Ingrese otro numero mas: '))

if num1 == (num2 + num3):
    print(str(num1) + " es = a " + str(num2) + " + " + str(num3))
    
elif num2 == (num1 + num3):
    print(str(num2) + " es = a " + str(num1) + " + " + str(num3))

elif num3 == (num1 + num2):
    print(str(num3) + " es = a " + str(num1) + " + " + str(num2))

else: 
    print('ningun numero es la suma de los otros 2.')