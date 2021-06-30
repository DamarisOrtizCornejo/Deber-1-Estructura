"""Diseñar un algoritmo tal que dados como datos dos variables de tipo entero,obtenga el resultado de la siguiente función"""
class ejercicio9:
        def __init__(self):
        	pass
        def VariablesEnt(self):
        	num = int(input("Ingrese la primera variable: " ))
        	V = int(input("Ingrese la segunda variable: " ))
        	print( )
        	if num == 1:
        		resp=(100*V)
        		if num == 2:
        		  resp=pow(100^V)
        		  if num == 3:
        		  	resp=(100/V)
        	else:
        	   resp=0
        	   print("Su resultado es: ", resp)
        	   print( )

resultado = ejercicio9()
resultado.VariablesEnt()