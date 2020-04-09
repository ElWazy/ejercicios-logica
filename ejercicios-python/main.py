from ejercicios.etc import validador
f = open('./descripcionEjercicios.txt', 'r')
for x in f:
    print(x)

opMenu = validador.validar('int', '\nDigite una opcion: ')

menu = True

while menu:
    if opMenu == 0:
        menu = False
    elif opMenu == 1:
        import ejercicios.ejercicio1
        menu = False
    elif opMenu == 2:
        import ejercicios.ejercicio2
        menu = False
    elif opMenu == 3:
        import ejercicios.ejercicio3
        menu = False
    elif opMenu == 4:
        import ejercicios.ejercicio4
        menu = False
    elif opMenu == 5:
        import ejercicios.ejercicio5
        menu = False
    elif opMenu == 7:
        import ejercicios.ejercicio7
        menu = False
    elif opMenu == 9:
        import ejercicios.ejercicio9
        menu = False
    elif opMenu == 11:
        import ejercicios.ejercicio11
        menu = False
    elif opMenu == 13:
        import ejercicios.ejercicio13
        menu = False
    elif opMenu == 17:
        import ejercicios.ejercicio17
        menu = False
    elif opMenu == 18:
        import ejercicios.ejercicio18
        menu = False
    else:
        print('ingrese un numero valido')
        menu = False