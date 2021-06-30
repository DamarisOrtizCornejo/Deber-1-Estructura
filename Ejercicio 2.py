"""En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra. Realize un programa en donde calcule el valor final por su compra"""
class Ejercicio2:
	def _init_(self):
		pass
def ejecutar( ):
	ToC = float(input("Ingrese el total de la compra: "))
	Desc = ToC*0.15
	CantP = ToC-Desc
	print("Su cantidad a pagar es: ")
	print(CantP, "$")
ejecutar( )