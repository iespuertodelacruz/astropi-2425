# /// script
# dependencies = [
#   "faker",
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
sense = SenseHat()
position = get_ISS_position()
print(position)

sense.set_imu_config(compass_enabled=True, gyro_enabled=False, accel_enabled=False)
magnetic = sense.get_compass_raw()
print(magnetic)
