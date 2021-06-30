"""Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero que no tiene más divisores que él mismo y la unidad. Elaborar Pseudocódigo"""       
class Bucle:
    def __init__(self):
    	pass                                        
    def num_primo(self):
        primo = True
        divisor = 2
        num= int(input("Ingrese un numero: "))
        while ((primo == True) and (divisor<num)):
        	if((num % divisor) == 0):
        		primo = "False";
        	else:
        		divisor =divisor+1;
        if(primo == "True"):
        	print("El numero ingresado es primo".format(num));
        else:
        	print("El numero ingresado no es primo".format(num));
        
bucles = Bucle()
bucles.num_primo()