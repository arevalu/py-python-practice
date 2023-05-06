# Convertir longitudes de millas a Km. y de pulgadas a cm., si:
# 1 milla = 1.60935 Km.
# 1 pulgada = 2.534 cm

CONVERSION_FACTOR_MILES_TO_KM = 1.60935
CONVERSION_FACTOR_INCHES_TO_CM = 2.534
DEFAULT_VALUE = "0"

miles = int(
    input("Ingresar la cantidad de millas que desea convertir a km: ") or DEFAULT_VALUE
)
inches = int(
    input("Ingrese la cantidad de pulgadas que desea convertir a cm: ") or DEFAULT_VALUE
)

if miles > 0:
    km = miles * CONVERSION_FACTOR_MILES_TO_KM
    print(f"> {miles} millas son {km} kilómetros")

if inches > 0:
    cm = inches * CONVERSION_FACTOR_INCHES_TO_CM
    print(f"> {inches} pulgadas son {cm} centimetros")
