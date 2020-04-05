# Generar un programa que muestre todos los múltiplos de 5,
# entre el rango 0 y 50.

contador = 0

while contador <= 50:
    if (contador % 5) == 0:
        print(contador)
    contador += 1