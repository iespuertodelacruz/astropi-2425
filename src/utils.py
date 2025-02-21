from math import atan2, cos, radians, sin, sqrt

from astro_pi_orbit import ISS


def calculate_distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    """
    Calculate the distance between two points on the Earth's surface using the Haversine formula.
    """
    EARTH_RADIUS = 6371.0  # Earth radius in kilometers

    lat1, lon1 = radians(point1[0]), radians(point1[1])
    lat2, lon2 = radians(point2[0]), radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS * c  # Distance in kilometers


def calculate_speed(
    point1: tuple[float, float], point2: tuple[float, float], time_interval: float
) -> float:
    """
    Calculate the speed of the ISS in km/s.
    """
    distance = calculate_distance(point1, point2)  # Distance in kilometers
    return distance / time_interval  # Speed in km/s


def get_ISS_position() -> dict:
    """
    Returns the current ISS latitude and longitude (degrees).
    """
    iss = ISS()
    point = iss.coordinates()
    lat = point.latitude.signed_dms()
    lon = point.longitude.signed_dms()
    return {'latitude': lat, 'longitude': lon}
