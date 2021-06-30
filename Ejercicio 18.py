"""Sea un vector “Calificaciones” de 100 componentes: En forma de columna se representaría así"""

class ejercicio18:
    def __init__(self):
    	pass                                    
    def arreglo1(self):
            calif = [ ]
            for i in range(20):
            	dato = int(input("Ingrese el dato {}: ".format(i)))
            	calif.append(dato)
            print("Las calificaciones son: {}".format(calif))                              
resultado=ejercicio18()
resultado.arreglo1()