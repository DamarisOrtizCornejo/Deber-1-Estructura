"""Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,utilizando un bucle controlado por centinela"""
class Bucles:
    def __init__(self):
        pass
    def control_centinela(self):
        su = 0
        prod = 1
        n = int(input("Ingrese un numero: "))
        while n != -1:
            su = su + n
            prod = prod * n
            print('CONTROLADO POR CENTINELA: Total suma: {}  -  Total producto: {}'.format(su,prod))
            n = int(input("Ingrese un numero"))
 bucles = Bucles( )                               
 bucles.control_centinela( )