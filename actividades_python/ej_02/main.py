from gpiozero import LED
from time import sleep

ledVerde = LED(13)
ledRojo = LED(19)
ledAzul = LED(26)

while True:
	sleep(0.25)
	ledVerde.on()
# enciende el led verde por 1/4 de segundo
	sleep(0.25)
	ledVerde.off()
	ledAzul.on()
# al pasar medio segundo se apaga el led verde y se enciende el led azul
	sleep(0.25)
	ledVerde.on()
	sleep(0.25)
	ledVerde.off()
	ledAzul.off()
	ledRojo.on()
# en el primer segundo se apaga s led verde y azul, y se enciende el rojo
# se repite el mismo ciclo
	sleep(0.25)
	ledVerde.on()
	sleep(0.25)
	ledVerde.off()
	ledAzul.on()
	sleep(0.25)
	ledVerde.on()
	sleep(0.25)
	ledVerde.off()
	ledAzul.off()
	ledRojo.off()
# se apagan los 3 leds y termina el código
