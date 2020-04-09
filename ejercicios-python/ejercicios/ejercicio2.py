from ejercicios.etc import validador
# Dados dos numeros reales. Indique cual es el mayor.
print('\n## EJERCICIO 2 ##\n')

num1 = validador.validar('float', '1')
num2 = validador.validar('float', '3')

if num1 > num2:
    print(str(num1) + ', es mayor que ' + str(num2))
else:
    print(str(num2) + ', es mayor que ' + str(num1))