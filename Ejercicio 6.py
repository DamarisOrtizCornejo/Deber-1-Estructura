"""Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento."""
class Ejercicio6:
    def __init__(self):
        pass
    def run( ):
        su = float(input("Ingrese el sueldo del empleado: $"))
        if su <=600:
            aum=su*0.10
            ns=su+aum
            print("Su nuevo sueldo es: $",ns)
        else:
        	print("Su sueldo es: $",su)

    run( )