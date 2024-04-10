tiempo = int(input("ingrese el tiempo en segundos (s): "))

horas = tiempo // 3600
minutos = (tiempo % 3600) // 60

print (f"el tiempo en horas de {tiempo} es: {horas}")
print (f"el tiempo en minutos de {tiempo} es: {minutos}")