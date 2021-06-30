"""Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa,   sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple"""
class Ejercicio7:
    def __init__(self):
        pass                                        
    def calcularJornada(self):
             ht, he, het=0,0,0       
             ph, phe, pt=0,0,0
             ht = int(input("Ingrese sus horas trabajadas: $ "))
             ph = float(input("Ingrese el valor por hora: $ "))
             if ht > 40:
                 he = ht-40                       
                 if he > 8:
                 	het = he-8
                 	phe = ph*2*8+ph*3*het
                 else:           
                     phe =ph*2*he             
                 pt = ph*40+phe
             else:
                 pt = ht*ph
              print("Sobretiempo<8: { } Sobretiempo>8: { } Jornada: { } ".format(ph,phe,pt))

tarea = Ejercicio7()
tarea.calcularJornada()