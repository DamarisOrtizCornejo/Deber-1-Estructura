"""Aplicar los pasos de la metodología para la solución de un problema para          leer un número entero N y calcular el resultado de la siguiente serie: 1- 1/2+1/3-1/4+....+-1/N"""
class Bucle:
    def __init__(self):
        pass
    def estruc_repeat(self):
        I=1
        serie=0
        num= int(input("Ingrese un numero: "))
        band=True
        while band:
            if band == True:
                serie=serie+(1/I)
                band=False
            else:
                serie=serie-(1/I)
                band=True
            I+=1
            if I>num:
                break
            print("El resultado de a serie es: {}" .format(serie))
calculo = Bucle()
calculo.estruc_repeat()