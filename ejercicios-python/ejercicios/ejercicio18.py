from time import sleep
from os import system
import platform

n=0
print()
so=platform.system()

print('este programa mostrara los nuemros hasta el infinito\npara salir tendra que terminar el proceso')
while 1:
    if(so=='Windows'):
       system('cls')
    if(so=='Linux'):
        system('clear')

    print(n)
    n+=1

    sleep(0.50)
