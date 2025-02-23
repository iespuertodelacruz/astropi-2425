# ==============================================================================
# Set of utility functions to help with the main program.
# ==============================================================================
from math import atan2, cos, radians, sin, sqrt

from astro_pi_orbit import ISS


def calculate_distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    """
    Calculate the distance between two points on the Earth's surface using the Haversine formula.
    """
    ISS_ORBIT_HEIGHT = 6371.0 + 400  # Earth radius in kilometers plus (ISS altitude is 400 km)

    lat1, lon1 = radians(point1[0]), radians(point1[1])
    lat2, lon2 = radians(point2[0]), radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return ISS_ORBIT_HEIGHT * c  # Distance in kilometers


def calculate_speed(
    point1: tuple[float, float], point2: tuple[float, float], time_interval: float
) -> float:
    """
    Calculate speed between two points on the Earth's surface.
    """
    distance = calculate_distance(point1, point2)  # Distance in kilometers
    return distance / time_interval  # Speed in km/s


def get_ISS_position() -> dict:
    """
    Get the current position of the International Space
    Station (ISS) in terms of latitude and longitude.
    """
    iss = ISS()
    point = iss.coordinates()
    lat = point.latitude.degrees
    lon = point.longitude.degrees
    return {'latitude': lat, 'longitude': lon}
