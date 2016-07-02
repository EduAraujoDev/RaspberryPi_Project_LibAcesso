#Programa: Testa o display 16x2
#Autor: Eduardo Araujo Dev

import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import time

tempo = 1

lcd_rs        = 18
lcd_en        = 23
lcd_d4        = 12
lcd_d5        = 16
lcd_d6        = 20
lcd_d7        = 21
lcd_backlight = 4


lcd_colunas = 16
lcd_linhas  = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_colunas, lcd_linhas, lcd_backlight)

try:
	while True:
		lcd.clear()

		message = 'DISPLAY 16X2'
		lcd.message(message);
		lcd.message('\nEDUARDO DEV')

		for i in range(lcd_colunas-len(message)):
			time.sleep(tempo)
			lcd.move_right()

		for i in range(lcd_colunas-len(message)):
			time.sleep(tempo)
			lcd.move_left()
except KeyboardInterrupt:
	lcd.clear()
	GPIO.cleanup()