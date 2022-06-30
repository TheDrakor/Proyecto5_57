#Proyecto 5
#--------------------------------------------------------------------------------------
saldo_actual = 0
Ingresos = []
Reintegros = []
#--------------------------------------------------------------------------------------
while True:
#--------------------------------------------------------------------------------------
	print("OPERATIVA CUENTA BANCARIA\n\n¿Qué deseas hacer?\n1- Ingreso\n2- Reintegro\n")
	opcion = float(input("Introduce una opcion: "))
#--------------------------------------------------------------------------------------
	if opcion == 1:
		cantidad = float(input("Introduce una cantidad: "))
		saldo_actual += cantidad
		print(f"\nSaldo: {saldo_actual}\n")
		Ingresos.append(cantidad)
#--------------------------------------------------------------------------------------
	elif opcion == 2:
		cantidad = float(input("Intsroduce una cantidad: "))
		if cantidad>saldo_actual:
			print("\nLo siento, no hay saldo suficiente.\n")
		else:
			saldo_actual -= cantidad
			print(f"\nSaldo: {saldo_actual}\n")
			Reintegros.append(-cantidad)
#--------------------------------------------------------------------------------------
	else:
		break
print(f"\nIngresos: {Ingresos}\nReintegros: {Reintegros}")
#--------------------------------------------------------------------------------------