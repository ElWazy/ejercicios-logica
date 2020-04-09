from ejercicios.etc import validador
import math
# Realizar programa para calcular la hipotenusa de un triángulo rectángulo, 
# conocidos sus 2 catetos.
a = validador.validar('int','1')
b = validador.validar('int', '2')

c = math.sqrt((a**2) + (b**2))

print(str(c))