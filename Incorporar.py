from Rotar import *


# RECOLECCION DE INFORMACION DE MOVIMIENTO

SPR = []
for i in range(3):
    SPR.append(input("Ingrese numero de pasos para el motor {} (200 pasos por vuelta): ".format(i+1)))

#IMPLEMENTACION DEL CONTROLADOR

Controlador = Rotar(SPR)
Controlador.conf_puertos()
Controlador.direccion()
Controlador.rot()
Controlador.escribir_coord()
