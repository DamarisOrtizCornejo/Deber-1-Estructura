#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.
class ejercicio11:
    def __init_(self):
        pass
    def cicloFor(self):
        i = 1
        su = 0
        for i in range(100):
            su=su+i*i
            print("La suma de los primeros 100 cuadrados es: ", su)

resultado=ejercicio11()
resultado.cicloFor()