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
from time import monotonic_ns, sleep, strftime

# ==============================================================================
if DEBUG:
    from fake_sensors import SenseHat, get_ISS_position
else:
    from sense_hat import SenseHat  # type: ignore

    from .utils import get_ISS_position

# ==============================================================================
OUT_PATH = 'iss.csv'
HOURS_RUNNIG = 3
HOUR2MIN = 60
MIN2SEC = 60
SEC2NANOSEC = 1_000_000_000


sense = SenseHat()
initial_time = monotonic_ns()
duration = HOURS_RUNNIG * HOUR2MIN * MIN2SEC * SEC2NANOSEC


# HEADER AND MEASURES VARIABLES
def format_data_fields(*, format: bool) -> str:
    """
    Choose True or False to select the format (header or variables).

    :param format: True (variable format) / False (header format).
    :type format: bool

    :return: text separated by commas or variables
    :rtype: str
    """

    measures = [
        f'{time}' if format else 'date_time_utc',
        f'{longitude}' if format else 'longitude',
        f'{altitude}' if format else 'altitude',
        f'{temperature}' if format else 'temperature',
        f'{humidity}' if format else 'humidity',
        f'{pressure}' if format else 'pressure',
        f'{mx}' if format else 'magnetic_field_x',
        f'{my}' if format else 'magnetic_field_y',
        f'{mz}' if format else 'magnetic_field_z',
        f'{ax}' if format else 'acceleration_x',
        f'{ay}' if format else 'acceleration_y',
        f'{az}' if format else 'acceleration_z',
        f'{rx}' if format else 'rotation_x',
        f'{ry}' if format else 'rotation_y',
        f'{rz}' if format else 'rotation_z',
    ]
    return f'{",".join(measures)}\n'


# FILE CODE
with open(OUT_PATH, 'w') as f:
    f.write(f'{format_data_fields(format=False)}')

    while (monotonic_ns() - initial_time) < (duration - SEC2NANOSEC):
        # VARIABLES

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

        f.write(f'{format_data_fields(format=True)}')
        sleep(1)
