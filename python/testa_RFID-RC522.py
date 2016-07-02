#Programa: Testa o leitor RFID-RC522
#Autor: Eduardo Araujo Dev

import RPi.GPIO as GPIO
import MFRC522

id_autorizado = [[104,62,174,16,232]]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MIFAREReader = MFRC522.MFRC522()

print 'Pressione Ctrl-C para encerrar a aplicacao.'

try:
	while True:
		(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

		if status == MIFAREReader.MI_OK:
			print 'Cartao detectado...'

			(status,uid) = MIFAREReader.MFRC522_Anticoll()

			print "Cartao lido UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+","+str(uid[4])

			if uid in id_autorizado:
				print 'Acesso Liberado'
			else:
				print 'Acesso Negado'
except KeyboardInterrupt:
	print 'Ctrl+C capturado, encerrando aplicacao.'
	GPIO.cleanup()