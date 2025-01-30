import random


def get_ISS_position() -> dict:
    """
    Returns the ISS latitude and longitude (degrees) and altitude (km).
    """
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    alt = random.uniform(400, 420)

    return {'latitude': lat, 'longitude': lon, 'altitude': alt}


class SenseHat:
    def get_temperature(self) -> float:
        return random.uniform(20, 30)

    def get_humidity(self) -> float:
        return random.uniform(40, 60)

    def get_pressure(self) -> float:
        return random.uniform(1000, 1020)

    def set_imu_config(self, **kwargs):
        pass

    def get_compass_raw(self):
        return {
            'x': random.uniform(-100, 100),
            'y': random.uniform(-100, 100),
            'z': random.uniform(-100, 100),
        }

    def get_gyroscope_raw(self):
        return {
            'x': random.uniform(-100, 100),
            'y': random.uniform(-100, 100),
            'z': random.uniform(-100, 100),
        }

    def get_accelerometer_raw(self):
        return {
            'x': random.uniform(-100, 100),
            'y': random.uniform(-100, 100),
            'z': random.uniform(-100, 100),
        }
