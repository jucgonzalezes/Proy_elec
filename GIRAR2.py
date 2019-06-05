
#FUNCION PARA MOVIMIENTO DE MOTORES----------------------------------------------------------- 

#Rotacion motor 0 y 1
def rot(Sentido, Sentido1, step_count):
        GPIO.output(DIR,Sentido)
        GPIO.output(DIR1,Sentido1)
        for x in range(step_count):
                GPIO.output(STEP,GPIO.HIGH) #activa para que de el paso espera desactiva espara y al siguiente paso
                GPIO.output(STEP1,GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP,GPIO.LOW)
                GPIO.output(STEP1,GPIO.LOW)
                sleep(delay)
                GPIO.output(LED,GPIO.HIGH) if x < step_count-1 else GPIO.output(LED,GPIO.LOW)
                GPIO.output(LED1, GPIO.HIGH) if x< step_count-1 else GPIO.output(LED1,GPIO.LOW)



#DECLARACION DE VARIABLES DE PARA LOS MOTORES--------------------------------------------------

#Motor 0

CW=1    #rotacion en direccion contraria del reloj
CCW=0   #rotacion en direccion del reloj
DIR = "P8_7" # Controlador de paso
STEP = "P8_9" # Controlador de direccion
LED = "P8_14" # Enciende el Bombillo


#Motor 1

CW1 =  1
CCW =  0
DIR1 = "P8_13"
STEP1 = "P8_11"
LED1 = "P8_16"


#Activar los puertos de los motores 0 y 1

GPIO.setup(DIR,GPIO.OUT) #activa el puerto de la direccion
GPIO.setup(STEP,GPIO.OUT) #Activa el puerto del paso
GPIO.setup(LED,GPIO.OUT) # Activa el puerto del LED


GPIO.setup(DIR1,GPIO.OUT)
GPIO.setup(STEP1,GPIO.OUT)
GPIO.setup(LED1,GPIO.OUT)


#SENTIDO Y PASO DE LOS MOTORES-------------------------------------------------------------------

#Motor 0. Pasos Sentido y Deley
SPR =2000# input("Ingrese SPR: ")  #pasos por revolucion
delay =0.01# input('Ingrese delay: ')           # tiempo que se demora en dar un paso


Sentido = CW  #input('Ingrese Sentido. CW para aClockwise y CCW para CounterClockwise: ')
step_count = SPR


Sentido1 = CW1
step_count1 = step_count



#ACTIVAR LA FUNCION DE ROTACION DE MOTORES-------------------------------------------------------

#rot(Sentido, step_count)
rot(Sentido, Sentido1, step_count)

GPIO.cleanup()



