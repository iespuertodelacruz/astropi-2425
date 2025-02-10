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
from time import sleep, strftime

# ==============================================================================
if DEBUG:
    from fake_sensors import SenseHat, get_ISS_position
else:
    from sense_hat import SenseHat  # type: ignore

    from .utils import get_ISS_position

# ==============================================================================
# VARIABLES
out_path = 'iss.csv'
boo_true = True
sense = SenseHat()

counter = 0

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
with open(out_path, 'w') as f:
    f.write(f'{",".join(HEADER)}\n')

    while counter < 10:
        # VARIABLES

        # NON XYZ
        time = strftime('%d-%b-%Y %H:%M:%S')
        latitude, longitude, altitude = get_ISS_position().values()
        temperature = sense.get_temperature()
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()

        # XYZ
        acceleration_x, acceleration_y, acceleration_z = sense.get_accelerometer_raw().values()
        magnetic_x, magnetic_y, magnetic_z = sense.get_compass_raw().values()
        rotation_x, rotation_y, rotation_z = sense.get_gyroscope_raw().values()
        counter += 1

        measures = [
            f'{time}',
            f'{latitude}',
            f'{longitude}',
            f'{altitude}',
            f'{temperature}',
            f'{humidity}',
            f'{pressure}',
            f'{magnetic_x}',
            f'{magnetic_y}',
            f'{magnetic_z}',
            f'{acceleration_x}',
            f'{acceleration_y}',
            f'{acceleration_z}',
            f'{rotation_x}',
            f'{rotation_y}',
            f'{rotation_z}',
        ]

        f.write(f'{",".join(measures)}\n')
        sleep(1)

with open(out_path) as lines:
    for line in lines:
        print(line)
        sleep(1)
