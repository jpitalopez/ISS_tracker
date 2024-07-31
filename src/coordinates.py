

import requests
import datetime

def get_iss_position(api_url: str = "http://api.open-notify.org/iss-now.json"):
    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(f"Error fetching ISS data: {e}")
        return None

    if data['message'] == 'success':
        # Extract the ISS location
        location = data["iss_position"]
        latitude = float(location['latitude'])
        longitude = float(location['longitude'])

        #print(f"Current coordinates - Latitude: {latitude}, Longitude: {longitude}")
        #print(f"Current time: {datetime.datetime.fromtimestamp(data['timestamp'])}")
        
        return latitude, longitude
    else:
        print("Failed to obtain ISS position data.")
        return None

# Ejemplo de uso
#coords = get_iss_position()

#if coords:
#    latitude, longitude = coords
#    print(f"Latitud: {latitude}, Longitud: {longitude}")