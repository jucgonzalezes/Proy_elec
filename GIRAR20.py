import Adafruit_BBIO.GPIO as GPIO
from time import sleep
import numpy as np

def rot(Motor,Sentido, step_count):
	GPIO.output(eval('DIR{}'.format(Motor)),Sentido)
	for x in range(step_count+1):
		print(x)
		for elem in ([1,0]):
			GPIO.output(eval('STEP{}'.format(Motor)),elem)
			sleep(delay)
		GPIO.output(eval('LED{}'.format(Motor)),GPIO.HIGH) if x < step_count-1 else GPIO.output(eval('LED{}'.format(Motor)),GPIO.LOW)



#Commit
#Commit2
#DECLARACION DE VARIABLES DE PARA LOS MOTORES--------------------------------------------------
CW, CCW=0, 1	#rotacion en direccion contraria (del) del reloj
DIR1, DIR2, DIR3 = "P8_7","P8_13","P8_13" # Puertos de direccion
STEP1,STEP2,STEP3 = "P8_9","P8_11","P8_11" # Puertos de paso
LED1, LED2, LED3 = "P8_14","P8_16","P8_16" # Puertos LED

for elm in np.arange(1,4):
	A=['DIR{}'.format(elm), 'STEP{}'.format(elm), 'LED{}'.format(elm)]
	for i in range(len(A)):
		GPIO.setup(eval(A[i]), GPIO.OUT)


#PARA EL PUNTO INICAL DE LOS MOTORES___________________________________________________________

volver_punto_inicial=open("punto_inicial.dat","r")
delay = 0.001#input('Ingrese delay: ')		# tiempo que se demora en dar un paso
#for line,i in zip(volver_punto_inicial,np.arange(1,4)):
#	coordenada_inicial = eval(volver_punto_inicial.readline())
#	rot("{}".format(i),CCW, coordenada_inicial)
#
volver_punto_inicial.close()





#SENTIDO Y PASO DE LOS MOTORES-------------------------------------------------------------------

SPR1 = input("Ingrese numero de pasos para el motor 1 (200 pasos por vuelta): ")  #pasos por revolucion
SPR2 = input("Ingrese numero de pasos para el motor 2 (200 pasos por vuelta): ")  #pasos por revolucion
SPR3 = input("Ingrese numero de pasos para el motor 3 (200 pasos por vuelta): ")  #pasos por revolucion


Dir = input('Direccion (CW o CCW): ')

rot("1",Dir,SPR1)
rot("2",Dir,SPR2)
rot("3",Dir,SPR3)


puntocero=open("puntos_iniciales.dat","w")
puntocero.write("{}\n,{}\n,{}".format(SPR1,SPR2,SPR3))
puntocero.close()



#ACTIVAR LA FUNCION DE ROTACION DE MOTORES-------------------------------------------------------
GPIO.cleanup()
