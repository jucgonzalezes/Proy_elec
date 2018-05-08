import Adafruit_BBIO.GPIO as GPIO
from time import sleep


def rot(Sentido, step_count):
	GPIO.output(DIR,Sentido)
	for x in range(step_count):
		print(x+1)
		GPIO.output(STEP,GPIO.HIGH) #activa para que de el paso espera desactiva espara y al siguiente paso
		sleep(delay)
		GPIO.output(STEP,GPIO.LOW)
		sleep(delay)
		GPIO.output(LED,GPIO.HIGH) if x<step_count else GPIO.output(LED,GPIO.LOW)


CW=1	#rotacion en direccion contraria del reloj
CCW=0	#rotacion en direccion del reloj
DIR = "P8_7" # Controlador de paso
STEP = "P8_9" # Controlador de direccion
LED = "P8_14" # Enciende el Bombillo



GPIO.setup(DIR,GPIO.OUT) #activa el puerto de la direccion
GPIO.setup(STEP,GPIO.OUT)	#activa el puerto del paso
GPIO.setup(LED,GPIO.OUT) # Activa el puerto del LED


SPR=input("Ingrese SPR: ")  #pasos por revolucion
delay=input('Ingrese delay: ')		# tiempo que se demora en dar un paso
Sentido = 1 #input('Ingrese Sentido. CW para Clockwise y CCW para CounterClockwise: ')

step_count=SPR

#rot(Sentido, step_count)
rot(Sentido, step_count)

GPIO.cleanup()
