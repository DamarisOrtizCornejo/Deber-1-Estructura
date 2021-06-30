"""Un vendedor recibe un sueldo base mas un 10% extra por comision de sus ventas. El vendedor desea saber cuanto dinero obtendra por conceoto de comisiones por las 3 ventas que realiza en el mes y el total que recibira en el mes tomando en cuenta su salario base y sus comisiones"""
class Ejercicio3:
	def run( ):
		Sb=float(input("Ingrese su salario base: "))
		V1=float(input("Ingrese el valor de la primera venta: "))
		V2=float(input("Ingrese el valor de la segunda venta: "))
		V3=float(input("Ingrese el valor de la tercera venta: "))
		TV=V1+V2+V3
		C=TV*0.10
		SR=Sb+C
		print("Su total del salario a recibir es: $ ", SR)
	run( )
