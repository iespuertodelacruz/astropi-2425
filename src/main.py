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
# IMPORTS
# ==============================================================================
if DEBUG:
    from fake_sensors import SenseHat, get_ISS_position
else:
    from sense_hat import SenseHat  # type: ignore

    from .utils import get_ISS_position

# ==============================================================================
# CODE
# ==============================================================================
HEADER = [
    'timestamp',
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
sense = SenseHat()


with open('iss.csv', 'w') as folder:
    folder.write(f'{','.join(HEADER)}\n')
    
    while True:
        timestamp = strftime('%d-%b-%Y %H:%M:%S')
        latitude, longitude, altitude = get_ISS_position().values()
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        
        acceleration_x, acceleration_y, acceleration_z = sense.get_accelerometer_raw().values()
        magnetic_x, magnetic_y, magnetic_z = sense.get_compass_raw().values()
        rotation_x, rotation_y, rotation_z = sense.get_gyroscope_raw().values()
        
parameters = [ 
    f'{timestamp}',
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

folder.write(f'{','.join(parameters)}\n')
time.sleep(5)