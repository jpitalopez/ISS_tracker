from angle_coords import angle_between_coords, deg_to_rad
from get_ISS_coordinates import get_iss_position
import math




def haversine(lat1, lon1, lat2, lon2):
    # Convertir grados a radianes
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Diferencias entre los puntos
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula del haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Radio de la Tierra en metros
    R = 6371000

    # Distancia en metros
    distancia = R * c

    return distancia


# Ejemplo de uso
lat1, lon1 = 41.3109, -4.9139  # Tu posición

coords = get_iss_position()

if coords:
    lat2, lon2 = coords
    
    # Altitud de la ISS en km

    print(haversine(lat1,lon1,lat2,lon2))


