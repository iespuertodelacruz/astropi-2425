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
from datetime import datetime
import time
if DEBUG:
    from fake_sensors import SenseHat, get_ISS_position
else:
    from sense_hat import SenseHat  # type: ignore

    from .utils import get_ISS_position
# ==============================================================================
# CODE
# ==============================================================================
sense = SenseHat()
sense.set_imu_config(compass_enabled=True, gyro_enabled=False, accel_enabled=False)
HEADER = ['timestamp', 'latitude', 'longitude', 'altitude', 'temperature', 'humidity', 'pressure', 'magnetic_x', 'magnetic_y', 'magnetic_z', 'acceleration_x', 'acceleration_y', 'acceleration_z', 'rotation_x', 'rotation_y', 'rotation_z']

with open('iss.csv', 'w') as f:
    f.write(f'{",".join(HEADER)}\n')
    
    while True:
        timestamp = datetime.now().isoformat()
        latitude, longitude, altitude = get_ISS_position().values()
        acceleration_x, acceleration_y, acceleration_z = sense.get_accelerometer_raw().values()
        magnetic_x, magnetic_y, magnetic_z = sense.get_compass_raw().values()
        rotation_x, rotation_y, rotation_z = sense.get_gyroscope_raw().values()
        temperature = sense.get_temperature()
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()
        position = get_ISS_position()
        
        f.write(f'{timestamp},{latitude},{longitude},{altitude},{temperature},{humidity},{pressure},{magnetic_x},{magnetic_y},{magnetic_z},{acceleration_x},{acceleration_y},{acceleration_z},{rotation_x},{rotation_y},{rotation_z}\n')
        time.sleep(5)