# Ingresar un número de tres cifras y mostrar el segundo dígito.

MESSAGE = "Ingresar número de tres cifras: "

number = input(MESSAGE)

while len(number) != 3:
    number = input(f"ERROR! {MESSAGE}")

print(f"El segundo dígito del número ingresado es {number[1]}")
