"""Dado como dato la calificacion de un alumno en un examen, escriba "aprobado" si si calificacion es nayor o igual que 7 y "Reprobado" en caso contrario"""
class Ejercicio5:
	def _init_(self):
		pass
	def run( ):
		calf = float(input("Ingrese su calificacion: "))
		if calf>=7:
			print("Aprobado")
			print("Felicidades, siga asi")
		else:
			print("Reprobado")
			print("Vuelva a intentarlo")
	run( )