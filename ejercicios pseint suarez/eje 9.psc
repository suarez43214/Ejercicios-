Algoritmo Valytotal
	escribir"digite valor unitario"
	leer val
	escribir "digite la cantidad de elementos comprados"
	leer pro
	subtotal <- val * pro
	iva<- subtotal*0.16
	total<-subtotal+iva
	escribir "el total de toda su compra es ", total
FinAlgoritmo
