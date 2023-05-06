# Hallar la longitud de la hipotenusa de un triángulo dada la medida de sus catetos.
import math

first_hick = float(input("Ingresar medida del primer cateto: "))
second_hick = float(input("Ingresar medida del segundo cateto: "))

# sqrt -> calcula raiz cuadrada
hypotenuse = math.sqrt(first_hick**2 + second_hick**2)

print(f"La hipotenusa del triángulo mide {hypotenuse}")
