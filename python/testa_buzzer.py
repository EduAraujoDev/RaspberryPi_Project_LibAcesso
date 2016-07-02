#Programa: Testa o buzzer
#Autor: Eduardo Araujo Dev

import RPi.GPIO as GPIO
import time

tempo = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT)

print 'Pressione Ctrl-C para encerrar a aplicacao.'

try:
	while True:
		GPIO.output(22, 0)
		print 'Buzzer ligado'

		time.sleep(tempo)

		GPIO.output(22, 1)
		print 'Buzzer desligado'

		time.sleep(tempo)
except KeyboardInterrupt:
	print 'Ctrl+C capturado, encerrando aplicacao.'

	GPIO.cleanup()