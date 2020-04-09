def validar(tipo, mensaje):
    while True:
        try:
            if tipo == 'int':
                # Mensajes predefinidos.
                if mensaje == '1':
                    value = int(input('Ingrese un numero: '))

                elif mensaje == '2':
                    value = int(input('Ingrese otro numero: '))
                
                elif mensaje == '3':
                    value = int(input('Ingrese otro numero mas: '))

                # Por defecto.
                else:
                    value = int(input(mensaje))

            elif tipo == 'str':
                value = input(mensaje)

            elif tipo == 'float':
                # Mensajes predefinidos.
                if mensaje == '1':
                    value = float(input('Ingrese un numero: '))

                elif mensaje == '2':
                    value = float(input('Ingrese otro numero: '))
                
                elif mensaje == '3':
                    value = float(input('Ingrese otro numero mas: '))

                # Por defecto.
                else:
                    value = float(input(mensaje))  
            
            else:
                print('Defina el tipo')

        except ValueError:
            print("Lo siento, no se puede procesar esa respuesta")
            continue
        else:
            break
    return value