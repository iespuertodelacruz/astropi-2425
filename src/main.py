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

# HEADER
HEADER = [
    'date_time_utc',
    'latitude',
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

# FILE CODE
with open(OUT_PATH, 'w') as f:
    f.write(f'{",".join(HEADER)}\n')

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

        # MEASURES
        measures = [
            f'{time}',
            f'{latitude}',
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

        f.write(f'{",".join(measures)}\n')
        sleep(1)
