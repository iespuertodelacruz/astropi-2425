# /// script
# dependencies = [
# ]
# ///

# ==============================================================================
# Astro Pi Challenge Mission Space Lab 2024/25
# ==============================================================================

"""
This is the main module of the project. It is the entry point of the program.
Team: Matraka, from IES Puerto de la Cruz - Telesforo Bravo
      Tenerife
      SPAIN
Members:
    - Carla
    - Daniele
    - Aarón

"""

DEBUG = True

# ==============================================================================
from datetime import datetime, timedelta
from time import sleep

# ==============================================================================
if DEBUG:
    from fake_sensors import SenseHat, get_ISS_position
else:
    from sense_hat import SenseHat  # type: ignore

    from .utils import get_ISS_position

# ==============================================================================
sense = SenseHat()

OUT_PATH = 'iss.csv'
HOURS_RUNNING = 2
MINUTES_RUNNIG = 59


def format_data_fields(*, format: bool) -> str:
    """
    Choose True or False to select the format (header or variables).

    :param format: True (variable format) / False (header format).
    :type format: bool

    :return: text separated by commas or variables
    :rtype: str
    """
    if not format:
        header = [
            'date_time_utc',
            'latitude',
            'longitude',
            'altitude',
            'temperature',
            'humidity',
            'pressure',
            'magnetic_x',
            'magnetic_y',
            'magnetic_z',
            'acceleration_x',
            'acceleration_y',
            'acceleration_z',
            'rotation_x',
            'rotation_y',
            'rotation_z',
        ]
        return ','.join(header) + '\n'
    else:
        variables = [
            f'{timestamp}',
            f'{position["latitude"]}',
            f'{position["longitude"]}',
            f'{position["altitude"]}',
            f'{temperature}',
            f'{humidity}',
            f'{pressure}',
            f'{magnetic["x"]}',
            f'{magnetic["y"]}',
            f'{magnetic["z"]}',
            f'{acceleration["x"]}',
            f'{acceleration["y"]}',
            f'{acceleration["z"]}',
            f'{rotation["x"]}',
            f'{rotation["y"]}',
            f'{rotation["z"]}',
        ]
        return ','.join(variables) + '\n'


with open(OUT_PATH, 'w') as f:
    f.write(format_data_fields(format=False))
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=MINUTES_RUNNIG)

    while datetime.now() < end_time:
        timestamp = datetime.now().isoformat()
        position = get_ISS_position()
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        sense.set_imu_config(compass_enabled=True, gyro_enabled=False, accel_enabled=False)
        magnetic = sense.get_compass_raw()
        sense.set_imu_config(compass_enabled=False, gyro_enabled=True, accel_enabled=False)
        rotation = sense.get_gyroscope_raw()
        sense.set_imu_config(compass_enabled=False, gyro_enabled=False, accel_enabled=True)
        acceleration = sense.get_accelerometer_raw()

        f.write(format_data_fields(format=True))
        f.flush()
        sleep(5)
