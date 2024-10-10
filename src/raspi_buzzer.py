


import RPi.GPIO as GPIO
import time

# Configurar la numeración de los pines
GPIO.setmode(GPIO.BCM)
zumbador_pin = 18  # Cambia esto al pin que estés utilizando

led_pin = 23  # Cambia esto al pin que estés utilizando

# Configurar el pin del LED como salida
GPIO.setup(led_pin, GPIO.OUT)

# Configurar el pin del zumbador como salida
GPIO.setup(zumbador_pin, GPIO.OUT)

# Configurar PWM en el pin del zumbador con una frecuencia de 1000 Hz (1 kHz)
pwm = GPIO.PWM(zumbador_pin, 700)  # Puedes cambiar la frecuencia según lo necesites

try:
    
    GPIO.output(led_pin, GPIO.HIGH)
    
    # Iniciar PWM con un ciclo de trabajo del 50%
    pwm.start(50)  # 50% de ciclo de trabajo

    # Mantener la frecuencia continua durante 3 segundos
    time.sleep(2)

    # Detener PWM
    pwm.stop()
    
    GPIO.output(led_pin, GPIO.LOW)
    
    time.sleep(0.2)
    
    GPIO.output(led_pin, GPIO.HIGH)
    
    time.sleep(0.2)
    
    GPIO.output(led_pin, GPIO.HIGH)
    
    time.sleep(0.2)
    
    GPIO.output(led_pin, GPIO.LOW)
    
    time.sleep(0.2)
    
    GPIO.output(led_pin, GPIO.HIGH)
    
    time.sleep(0.2)
    
    GPIO.output(led_pin, GPIO.LOW)
    
    
    
    

finally:
    # Limpiar la configuración de GPIO
    GPIO.cleanup()
