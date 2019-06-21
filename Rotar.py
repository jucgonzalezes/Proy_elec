# import Adafruit_BBIO.GPIO as GPIO
from time import sleep


class Rotar:
    def __init__(self, step_count=None):
        self.step_count = step_count
        self.vec = [1, 2, 3]
        self.coord_inic = self.leer_coord()
        print(self.coord_inic)
        print('Working well!')

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

    def direccion(self):
        for elem in self.vec:
            if eval(self.step_count[elem-1]) <= eval(self.coord_inic[elem-1]):
                #GPIO.output(eval('DIR{}'.format(elem)),0)
                print('El motor {} gira CW'.format(elem))
            else:
                #GPIO.output(eval('DIR{}'.format(elem)),1)
                print('El motor {} gira CCW'.format(elem))

    def conf_puertos(self):
        for elm in self.vec:
            print(elm)
            a = ['DIR{}'.format(elm), 'STEP{}'.format(elm), 'LED{}'.format(elm)]
            for k in range(len(a)):
                # GPIO.setup(eval(A[k]), GPIO.OUT)
                print(a[k])

    def rot(self):
        sprs = [eval(steps) for steps in self.step_count]
        for j in range(1, max(sprs) + 1):
            print('SPR: {}'.format(j))
            for motor in self.vec:
                if sprs[motor-1] >= j:
                    self.paso(motor)
                    print('Motor: {}'.format(motor))
            print('')


SPR = []
for i in range(3):
    SPR.append(input("Ingrese numero de pasos para el motor {} (200 pasos por vuelta): ".format(i+1)))


x = Rotar(SPR)
x.rot()
x.direccion()
