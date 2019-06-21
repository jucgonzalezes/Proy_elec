# import Adafruit_BBIO.GPIO as GPIO
from time import sleep


class Rotar:
    def __init__(self, step_count=None):
        self.step_count = step_count
        self.vec = [1, 2, 3]
        self.coord_inic = self.leer_coord()
        self.coord_rel = [abs(eval(steps)-eval(self.coord_inic[i])) for i, steps in enumerate(self.step_count)]

    @staticmethod
    def paso(motor):
        delay = 0.0001
        for elem in ([1, 0]):
            # GPIO.output(eval('STEP{}'.format(motor)), elem)
            sleep(delay)
        # print('paso para motor {}'.format(motor))

    @staticmethod
    def leer_coord():
        with open('puntos_iniciales.dat', 'r') as f:
            coord_inic = f.read().splitlines()
        return coord_inic

    def escribir_coord(self):
        with open('puntos_iniciales.dat', 'w') as f:
            f.write("{}\n{}\n{}".format(self.step_count[0], self.step_count[1], self.step_count[2]))

    def conf_puertos(self):
        for elm in self.vec:
            print(' ')
            print('Puertos designados para el motor {}'.format(elm))
            print(' ')
            a = ['DIR{}'.format(elm), 'STEP{}'.format(elm), 'LED{}'.format(elm)]
            for k in range(len(a)):
                # GPIO.setup(eval(A[k]), GPIO.OUT)
                print('{} = {}'.format(a[k], eval(a[k])))

    def direccion(self):
        print(' ')
        print('Direcciones de movimiento de cada motor')
        print(' ')
        for elem in self.vec:
            if eval(self.step_count[elem-1]) <= eval(self.coord_inic[elem-1]):
                # GPIO.output(eval('DIR{}'.format(elem)),0)
                print('El motor {} gira CW'.format(elem))
            else:
                # GPIO.output(eval('DIR{}'.format(elem)),1)
                print('El motor {} gira CCW'.format(elem))
        print(' ')

    def rot(self):
        print(' ')
        print('Inicia el movimiento')
        print(' ')
        for j in range(1, max(self.coord_rel) + 1):
            print('SPR: {}'.format(j))
            for motor in self.vec:
                if self.coord_rel[motor-1] >= j:
                    self.paso(motor)
                    print('Motor: {}'.format(motor))
            print('')

# DECLARACION DE LOS PUERTOS

DIR1, DIR2, DIR3 = "P8_7", "P8_13", "P8_13"  # Puertos de direccion
STEP1, STEP2, STEP3 = "P8_9", "P8_11", "P8_11"  # Puertos de paso
LED1, LED2, LED3 = "P8_14", "P8_16", "P8_16"  # Puertos LED

# GPIO.cleanup()
