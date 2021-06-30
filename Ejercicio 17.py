"""Calcular el factorial de N números enteros leídos de teclado. El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número"""
class Bucle:
    def __init__(self):
    	pass
    def bucle_anidado(self):
        num = int(input("Ingrese un numero: "))
        fact = 1
        for i in range(1, num+1):
        	fact *= i
        print("El factorial del numero {} es: {} ".format(num, fact))

calculo = Bucle()
calculo.bucle_anidado()