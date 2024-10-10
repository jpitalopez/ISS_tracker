import RPi.GPIO as GPIO
import time

# Configurar la numeración de los pines
GPIO.setmode(GPIO.BCM)
led_pin = 23  # Cambia esto al pin que estés utilizando

# Configurar el pin del LED como salida
GPIO.setup(led_pin, GPIO.OUT)

try:
    # Encender el LED
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(5)  # Mantener encendido durante 5 segundos

    # Apagar el LED
    GPIO.output(led_pin, GPIO.LOW)

finally:
    # Limpiar la configuración de GPIO
    GPIO.cleanup()
