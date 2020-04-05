f = open('descripcionEjercicios.txt', 'r')
for x in f:
    print(x)

while True:
    try:
        opMenu = int(input('\n\ningrese el numero del ejercicio que desea revisar: '))
    except ValueError:
        print("Lo siento, no se puede procesar esa respuesta")
        continue
    else:
        break

menu = True

while menu:
    if opMenu == 1:
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
    else:
        print('ingrese un numero valido')
        menu = False