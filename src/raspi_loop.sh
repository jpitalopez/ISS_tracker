


#!/bin/bash

# Ruta al programa de Python
programa_python="raspi_main.py"

while true; do
    # Ejecutar el programa de Python
    python3 $programa_python

    # Esperar 30 minutos (1800 segundos)
    sleep 300
done
