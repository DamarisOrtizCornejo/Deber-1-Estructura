"""Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres."""

class ejercicio8:
    def __init__(self):
        pass
    def NuMay(self):
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segudo numero : "))
        n3 = int(input("Ingrese el tercer numero : "))
        if n1 > n2 and n1 > n3:
            numa = n1
        else:
            if n2 > n3:
                numa = n2
            else:
                numa = n3
        print("El numero mayor es:", numa)
ejercicio = ejercicio8( )
ejercicio.NuMay( )
