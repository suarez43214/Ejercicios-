#calcular raiz cuadrada

num = float(input("ingrese el numero: "))

if num < 0:
    print("la raiz no se puede calcular: ")

else: raiz = num ** 0.5
print (f"la raiz cuadrada de {num} es: {raiz}")