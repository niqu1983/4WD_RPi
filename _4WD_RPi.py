from gpiozero import PWMLED

led1 = PWMLED(4)
led2 = PWMLED(17)
led3 = PWMLED(27)
led4 = PWMLED(22)


def FWD():
    led1.value = 1
    led2.value = 0
    led3.value = 1
    led4.value = 0

def RVS():
    led1.value = 0
    led2.value = 1
    led3.value = 0
    led4.value = 1

def LFT():
    led1.value = 1
    led2.value = 1
    led3.value = 0
    led4.value = 0

def RGT():
    led1.value = 0
    led2.value = 0
    led3.value = 1
    led4.value = 1
