# Generar un programa que muestre los numeros primos hasta el infinito.
from time import sleep
from os import system
import platform

print('\n## EJERCICIO 18 ##\n')

num1 = 0
so = platform.system()

print('para salir tendra que terminar el proceso\n')
while 1:
    if(so=='Windows'):
       system('cls')
    if(so=='Linux'):
        system('clear')

    print(num1)
    num1 += 1

    sleep(0.50)
