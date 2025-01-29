from orbit import ISS
from skyfield.api import load


def get_ISS_position() -> dict:
    """
    Returns the ISS latitude and longitude (degrees) and altitude (km).
    """
    position = ISS.at(load.timescale().now())
    location = position.subpoint()

    lat = location.latitude.degrees
    lon = location.longitude.degrees
    alt = location.elevation.km

    return {'latitude': lat, 'longitude': lon, 'altitude': alt}
