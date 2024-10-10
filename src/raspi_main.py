

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
from getdistance_ISS import getIssdistance

# Configuración de pines de Raspberry Pi
RST = 24
# Nota: los siguientes solo se usan con SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display con hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Inicializa la librería.
disp.begin()

# Limpia la pantalla.
disp.clear()
disp.display()

# Crea una imagen en blanco para dibujar.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))



# Obtén el objeto para dibujar.
draw = ImageDraw.Draw(image)

# Dibuja un fondo negro para borrar cualquier contenido previo.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Define la fuente para el texto.
font = ImageFont.load_default()

# Set your coordinates hear

lat1, lon1 = 41.3109, -4.9139


# Define el número y la frase a mostrar.
ISS_distance_km = getIssdistance(lat1,lon1)/1000
frase = "Hola, Raspberry Pi!"

# Dibuja el número y la frase en la pantalla.
draw.text((3, 8), f"Distancia ISS: ", font=font, fill=255)
draw.text((3, 18), f"{ISS_distance_km:.2f} km", font=font, fill=255)

# Muestra la imagen en la pantalla OLED.
disp.image(image)
disp.display()


if (ISS_distance_km<1500):
	import raspi_buzzer_led


