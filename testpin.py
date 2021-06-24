import RPi.GPIO as GPIO
import time
GPIOnum = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIOnum, GPIO.OUT)
GPIO.output(GPIOnum, GPIO.HIGH)
time.sleep(3)
GPIO.output(GPIOnum, GPIO.LOW)
GPIO.cleanup()