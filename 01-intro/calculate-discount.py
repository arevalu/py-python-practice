# Calcular el importe que debe pagar una persona compra una heladera de pesos X y por pagar en efectivo le hacen el 10% de descuento ¿Cuánto abona?

DISCOUNT = 10
PERCENTAGE = 100

purchase_price = float(input("Ingresa el valor de la compra: "))

discount_price = purchase_price * (DISCOUNT / PERCENTAGE)
price_with_discount = purchase_price - discount_price

print("El precio a pagar en efectivo es de $ ", price_with_discount)
