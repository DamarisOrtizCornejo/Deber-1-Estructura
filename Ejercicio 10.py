"""Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2.El aspirante que obtenga calificaciones mayores que 80 en ambos examenes es aceptado; caso contrario es rechazado."""

class ejercicio10:
    def __init__(self):
        pass
    def calificaciones(self):
        calf1=float(input("Ingrese la primera calificacion: " ))
        calf2=float(input("Ingrese la segunda calificacion: "))
        if(calf1 >= 80) and (calf2 >=80):
            print("Aceptado")
        else:
            print("Rechazado")
ejercicio=ejercicio10( )
ejercicio.calificaciones( )