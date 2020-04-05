# Generar un programa que indique cuantas notas (N)
# quiere calcular y que luego determine el promedio de estas N notas.

longitud = int(input('Ingrese su cantidad de notas: '))

contador = 1
suma = 0
while contador <= longitud:
    nota = int(input('Ingrese su nota'))
    suma += nota
    contador += 1

promedio = suma / longitud

print(promedio)