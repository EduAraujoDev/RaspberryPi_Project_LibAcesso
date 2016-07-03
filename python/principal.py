#Programa: Programa principal do controlador de acesso
#Autor: Eduardo Araujo Dev

import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import MFRC522
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(17, 0)
GPIO.output(27, 0)

lcd_rs        	= 18
lcd_en        	= 23
lcd_d4        	= 12
lcd_d5        	= 16
lcd_d6        	= 20
lcd_d7        	= 21
lcd_backlight	= 4
lcd_colunas		= 16
lcd_linhas		= 2
tempo			= 1
id_autorizado 	= [[104,62,174,16,232]]

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_colunas, lcd_linhas, lcd_backlight)

MIFAREReader = MFRC522.MFRC522()

print 'Pressione Ctrl-C para encerrar a aplicacao.'

def acendeled(pino_led):
	GPIO.output(pino_led, 1)
	return

def apagaled(pino_led):
    GPIO.output(pino_led, 0)
    return

try:
	acendeled(17)

	while True:
		lcd.clear()

		lcd.message('  DISPLAY 16X2  \n')
		lcd.message(' PASSE O CARTAO \n')

		(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

		if status == MIFAREReader.MI_OK:
			print 'Cartao detectado...'

			GPIO.output(22, 0)

			(status,uid) = MIFAREReader.MFRC522_Anticoll()

			print "Cartao lido UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+","+str(uid[4])

			if uid in id_autorizado:
				apagaled(17)
				acendeled(27)

				lcd.clear()
				lcd.message('  DISPLAY 16X2  \n')
				lcd.message(' ACESSO LIBERADO \n')

				time.sleep(tempo)

				apagaled(27)
				acendeled(17)

				print 'Acesso Liberado'
			else:
				lcd.clear()
				lcd.message('  DISPLAY 16X2  \n')
				lcd.message(' ACESSO  NEGADO  \n')

				time.sleep(tempo)

				print 'Acesso Negado'

		GPIO.output(22, 1)
		time.sleep(tempo)
except KeyboardInterrupt:
	print 'Ctrl+C capturado, encerrando aplicacao.'

	lcd.clear()
	GPIO.cleanup()