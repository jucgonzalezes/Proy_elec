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
#DECLARACION DE VARIABLES DE PARA LOS MOTORES--------------------------------------------------
CW, CCW=1, 0	#rotacion en direccion contraria (del) del reloj
DIR1, DIR2, DIR3 = "P8_7","P8_13","P8_13" # Puertos de direccion
STEP1,STEP2,STEP3 = "P8_9","P8_11","P8_11" # Puertos de paso
LED1, LED2, LED3 = "P8_14","P8_16","P8_16" # Puertos LED
#Inicializacion de los puertos de salida
for elm in np.arange(1,4):
	A=['DIR{}'.format(elm), 'STEP{}'.format(elm), 'LED{}'.format(elm)]
	for i in range(len(A)):
		GPIO.setup(eval(A[i]), GPIO.OUT)
#SENTIDO Y PASO DE LOS MOTORES-------------------------------------------------------------------
SPR = input("Ingrese numero de pasos (200 pasos por vuelta): ")  #pasos por revolucion
Motor = input('Ingrese el motor a mover (1,2 o 3): ')
delay = 0.001#input('Ingrese delay: ')		# tiempo que se demora en dar un paso
#ACTIVAR LA FUNCION DE ROTACION DE MOTORES-------------------------------------------------------
rot(Motor, CW, SPR)
GPIO.cleanup()
