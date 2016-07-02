#Programa: Testa os leds
#Autor: Eduardo Araujo Dev

import RPi.GPIO as GPIO
import time

tempo = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT) #led vermelho
GPIO.setup(27, GPIO.OUT) #led verde

GPIO.output(17, 0)
GPIO.output(27, 0)

print 'Pressione Ctrl-C para encerrar a aplicacao.'

def acendeled(pino_led):
	if pino_led == 17:
		print 'Led vermelho ligado'
	elif pino_led == 27:
		print 'Led verde ligado'

	GPIO.output(pino_led, 1)
	return

def apagaled(pino_led):
    GPIO.output(pino_led, 0)
    return

try:
	while True:      
	  acendeled(17)

	  time.sleep(tempo)

	  apagaled(17)
	  acendeled(27)

	  time.sleep(tempo)

	  apagaled(27)
except KeyboardInterrupt:
	print 'Ctrl+C capturado, encerrando aplicacao.'

	GPIO.cleanup()