# RaspberryPi_Project_LibAcesso
Projeto com exemplo de uma protopitapação para um sistema de liberação de acesso usando Raspberry pi B+ e Python. Para essa projetos, foi usado os seguintes componentes:

 - Protoboard 830 pontos
 - Led vermelho e verde
 - Resistores 10KΩ
 - Display LCD 16x2
 - Potenciômetro Trimpot 10KΩ
 - Buzzer
 - Leitor Rfid Mfrc522 Mifare (com alguns cartões para testes)
 - Jumper Macho-Macho e Macho-Femea

### Diagramação

Abaixo a diagramação do projeto usando o Fritzing

![](http://eduaraujodev.com/imagens/Project_LibAcesso.jpg)

### Observações

 - Instalações basica:

```sh
# apt-get update
# apt-get install build-essential python-dev python-smbus python-pip  git
# pip install RPi.GPIO
```
 - Para instalar a biblioteca do display 16x2:

```sh
# git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
# cd Adafruit_Python_CharLCD
# python setup.py install
```

 - Para instalar a biblioteca do Leitor Rfid Mfrc522, seguir os passos na página [https://github.com/EduAraujoDev/MFRC522-python].

 - Por padrão, ao iniciar o respbian o driver so SPI não iniciar automaticamente, sendo necessario remove-lo da blacklist

```sh
# vim /etc/modprobe.d/raspi-blacklist.conf
```

Caso contrario, para iniciar manualmente o driver

```sh
# modprobe spi-bcm2708
```