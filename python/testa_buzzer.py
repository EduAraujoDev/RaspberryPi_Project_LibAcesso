#Programa: Testa o buzzer
#Autor: Eduardo Araujo Dev

import RPi.GPIO as GPIO
import time

tempo = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT)

try:
	while True:
		GPIO.output(22, 0)

		time.sleep(tempo)

		GPIO.output(22, 1)

		time.sleep(tempo)
except KeyboardInterrupt:
	GPIO.cleanup()