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
from time import sleep, strftime

# ==============================================================================
if DEBUG:
    from fake_sensors import SenseHat, get_ISS_position
else:
    from sense_hat import SenseHat  # type: ignore

    from .utils import get_ISS_position

# ==============================================================================
OUT_PATH = 'iss.csv'
HOURS_RUNNING = 2
MUNUTES_RUNNIG = 59
SECONDS_RUNNING = 50

sense = SenseHat()
start_time = datetime.now()
end_time = start_time + timedelta(
    hours=HOURS_RUNNING, minutes=MUNUTES_RUNNIG, seconds=SECONDS_RUNNING
)


# HEADER AND MEASURES VARIABLES
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
            'longitude',
            'altitude',
            'temperature',
            'humidity',
            'pressure',
            'magnetic_field_x',
            'magnetic_field_y',
            'magnetic_field_z',
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
            f'{time}',
            f'{longitude}',
            f'{altitude}',
            f'{temperature}',
            f'{humidity}',
            f'{pressure}',
            f'{mx}',
            f'{my}',
            f'{mz}',
            f'{ax}',
            f'{ay}',
            f'{az}',
            f'{rx}',
            f'{ry}',
            f'{rz}',
        ]

        return ','.join(variables) + '\n'


# FILE CODE
with open(OUT_PATH, 'w') as f:
    f.write(format_data_fields(format=False))

    while start_time < end_time:
        # VARIABLES
        start_time = datetime.now()

        # NON XYZ
        time = strftime('%x %X')
        latitude, longitude, altitude = get_ISS_position().values()
        temperature = sense.get_temperature()
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()

        # XYZ
        # MAGNETIC FIELD
        sense.set_imu_config(compass_enabled=True, gyro_enabled=False, accel_enabled=False)
        magnetic = sense.get_compass_raw()
        mx = magnetic['x']
        my = magnetic['y']
        mz = magnetic['z']
        # ACCELERATION
        sense.set_imu_config(compass_enabled=False, gyro_enabled=False, accel_enabled=True)
        acceleration = sense.get_accelerometer_raw()
        ax = acceleration['x']
        ay = acceleration['y']
        az = acceleration['z']
        # ROTATION
        sense.set_imu_config(compass_enabled=False, gyro_enabled=True, accel_enabled=False)
        rotation = sense.get_gyroscope_raw()
        rx = rotation['x']
        ry = rotation['y']
        rz = rotation['z']

        f.write(format_data_fields(format=True))
        sleep(5)
