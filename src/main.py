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
from datetime import datetime, timedelta
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
HEADER = ['timestamp', 'latitude', 'longitude', 'altitude', 'temperature', 'humidity', 'pressure', 'magnetic_x', 'magnetic_y', 'magnetic_z', 'acceleration_x', 'acceleration_y', 'acceleration_z', 'rotation_x', 'rotation_y', 'rotation_z']

with open('iss.csv', 'w') as f:
    f.write(f'{",".join(HEADER)}\n')
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=3)
    
    while start_time < end_time:
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
        stats = [timestamp, position["latitude"], position["longitude"], position["altitude"], temperature, humidity, pressure, magnetic["x"], magnetic["y"], magnetic["z"], acceleration["x"], acceleration["y"], acceleration["z"], rotation["x"], rotation["y"], rotation["z"]]
        f.write(f'{",".join(stats)}\n')
        f.flush()
        time.sleep(5)