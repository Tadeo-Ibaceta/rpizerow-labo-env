from gpiozero import LED
from gpiozero import Buzzer

buzzer = Buzzer(15)
ledVerde = LED(13)
ledRojo = LED(19)
ledAzul = LED(26)

while True:
	accion = input()
	if 'buzz' in accion:
		if 'on' in accion:
			buzzer.on()
		elif 'off' in accion:
			buzzer.off()
	elif 'RGB' in accion:
		if 'blue' in accion: 
			ledAzul.toggle()
		elif 'red' in accion:
			ledRojo.toggle()
		elif 'green' in accion:
			ledVerde.toggle()
