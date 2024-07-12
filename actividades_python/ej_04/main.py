import gpiozero
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

red_led = PWMLED(17)
blue_led = PWMLED(27)

R_REF = 10000.0  # Resistencia de referencia
BETA = 3900.0    # Beta del termistor

GAIN = 1

def main():
	while True:
        	temp_setpoint = read_potentiometer()
        	actual_temp = read_thermistor()
        	control_leds(temp_setpoint, actual_temp)
        	print(f"Setpoint: {temp_setpoint:.2f}°C, Actual: {actual_temp:.2f}°C")
        	time.sleep(1)

def read_potentiometer():
    	# Leer valores de ADC
    	value = adc.read_adc(0, gain=GAIN)
	# Escalar el valor a un rango de 0 a 30 grados
    	temperature_setpoint = value * 30.0 / 32767.0
    	return temperature_setpoint

def read_thermistor():
   	# Leer valor del termistor
	value = adc.read_adc(1, gain=GAIN)
	# Convertir el valor del termistor a grados usando la ecuación de Steinhart-Hart
	resistance = R_REF * (32767.0 / value - 1.0)
	temperature = 1.0 / (1.0 / 298.15 + (1.0 / BETA) * (resistance / R_REF - 1.0)) - 273.15
	return temperature

def control_leds(temp_setpoint, actual_temp):
	difference = actual_temp - temp_setpoint
	max_difference = 5.0
	duty_cycle = min(abs(difference) / max_difference, 1.0)

	if difference > 0:
		# Enciende el LED azul cuando la temperatura real está por encima de la establecida
		blue_led.value = duty_cycle
        	red_led.value = 0
    	else:
        	# Enciende el LED rojo cuando la temperatura real está por debajo de la establecida
        	red_led.value = duty_cycle
        	blue_led.value = 0


if __name__ == "__main__":
	main()
