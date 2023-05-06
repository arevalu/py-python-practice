# Calcular el sueldo de una persona, conociendo la cantidad de horas que trabaja en el mes y el valor de la hora.

hours = int(input("Ingresar cantidad de horas trabajadas por mes: "))
value_per_hour = int(input("Ingresar valor por hora: "))

salary = hours * value_per_hour

print("El sueldo es de $", salary)
