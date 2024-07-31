import math

def deg_to_rad(deg):
    return deg * (math.pi / 180)

def angle_between_coords(lat1, lon1, lat2, lon2):
    # Convert coordinates from degrees to radians
    lat1 = deg_to_rad(lat1)
    lon1 = deg_to_rad(lon1)
    lat2 = deg_to_rad(lat2)
    lon2 = deg_to_rad(lon2)
    
    # Calculate the components of the vectors
    x1 = math.cos(lat1) * math.cos(lon1)
    y1 = math.cos(lat1) * math.sin(lon1)
    z1 = math.sin(lat1)
    
    x2 = math.cos(lat2) * math.cos(lon2)
    y2 = math.cos(lat2) * math.sin(lon2)
    z2 = math.sin(lat2)
    
    # Calculate the dot product and magnitudes of the vectors
    dot_product = x1 * x2 + y1 * y2 + z1 * z2
    magnitude1 = math.sqrt(x1**2 + y1**2 + z1**2)
    magnitude2 = math.sqrt(x2**2 + y2**2 + z2**2)
    
    # Calculate the angle using the dot product and magnitudes
    angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))
    
    # Convert the angle from radians to degrees
    angle_deg = angle_rad * (180 / math.pi)
    
    return angle_deg

# Ejemplo de uso
#lat1, lon1 = 40.7128, -74.0060  # Nueva York
#lat2, lon2 = 39.9526, -75.1652 # Los Ángeles

#angle = angle_between_coords(lat1, lon1, lat2, lon2)
#print(f"El ángulo entre las dos coordenadas es: {angle:.2f} grados")