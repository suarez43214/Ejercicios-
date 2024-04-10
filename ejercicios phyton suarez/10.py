salario_diario = float(input("ingrese el salario: "))
numero_de_dias_trabajo = int(input("ingrese numero de dias trabajados: "))

salario_bruto = salario_diario * numero_de_dias_trabajo
des_pension = salario_bruto * 0.10
des_salud = salario_bruto * 0.15
salario_neto = salario_bruto - des_pension - des_salud

print (f"el empleado tiene que pagar {salario_neto}")