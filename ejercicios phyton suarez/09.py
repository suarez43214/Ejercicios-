valor_unitario = int(input("ingrese el valor unitario: "))
cantidad = float (input("elementos comprados: "))

subtotal = valor_unitario * cantidad
iva = subtotal * 0.16
total = subtotal + iva

print (f"total = {total}")