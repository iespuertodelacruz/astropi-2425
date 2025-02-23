# ==============================================================================
# Astro Pi Challenge Mission Space Lab 2024/25
# ==============================================================================

"""
This is the main module of the project. It is the entry point of the program.
Team: Matraka, from IES Puerto de la Cruz - Telesforo Bravo (Tenerife, SPAN)
Members:
    - Carla
    - Daniele
    - Aarón
Email contact: 38003999@gobiernodecanarias.org
"""

# ==============================================================================
# IMPORTS
# ==============================================================================

# Import the necessary modules
from datetime import datetime, timedelta

# Import the Sense HAT library
from sense_hat import SenseHat

# Import the necessary functions from the utils module
from utils import calculate_speed, get_ISS_position

# ==============================================================================
# CONSTANTS AND CONFIGURATIONS
# ==============================================================================

OUT_PATH = 'iss_matraka.csv'  # Output file path
RESULT_PATH = 'result.txt'  # Result file path
DURATION_SECONDS = 9 * 60 + 30  # Duration of the experiment in seconds
INTERVAL = 5  # Interval in seconds for saving data
ROUNDING_DECIMALS = 4  # Number of decimal places to round the speed
HEADER = [  # CSV header
    'date_time_utc',
    'latitude',
    'longitude',
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
    'speed',
]

# ==============================================================================
# MAIN PROGRAM
# ==============================================================================

sense = SenseHat()  # Sense HAT object

# Open the output file and the speed log file
with open(OUT_PATH, 'w') as f:
    # Write headers
    f.write(','.join(HEADER) + '\n')

    # Start and end time of the experiment
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=DURATION_SECONDS)

    prev_position = None
    prev_time = None
    total_speed = []

    # Main loop
    while datetime.now() < end_time:
        timestamp = datetime.now().isoformat()
        position = get_ISS_position()

        # Sampling interval
        if prev_position is not None and prev_time is not None:
            time_diff = (datetime.now() - prev_time).total_seconds()
            if time_diff >= INTERVAL:
                # Calculate ISS Speed
                speed = calculate_speed(
                    (prev_position['latitude'], prev_position['longitude']),
                    (position['latitude'], position['longitude']),
                    time_diff,
                )
                total_speed.append(speed)

                # Get sensor data
                temperature = sense.get_temperature()  # Temperature in Celsius
                humidity = sense.get_humidity()  # Humidity in percentage
                pressure = sense.get_pressure()  # Pressure in millibars
                sense.set_imu_config(compass_enabled=True, gyro_enabled=False, accel_enabled=False)
                magnetic = sense.get_compass_raw()  # Magnetic field in microteslas
                sense.set_imu_config(compass_enabled=False, gyro_enabled=True, accel_enabled=False)
                rotation = sense.get_gyroscope_raw()  # Rotation in radians per second
                sense.set_imu_config(compass_enabled=False, gyro_enabled=False, accel_enabled=True)
                acceleration = sense.get_accelerometer_raw()  # Acceleration in Gs

                # Save data to the output file
                f.write(
                    f'{timestamp},{position["latitude"]},{position["longitude"]},{temperature},'
                    f'{humidity},{pressure},{magnetic["x"]},{magnetic["y"]},{magnetic["z"]},'
                    f'{acceleration["x"]},{acceleration["y"]},{acceleration["z"]},'
                    f'{rotation["x"]},{rotation["y"]},{rotation["z"]},{speed}\n'
                )
                f.flush()

                # Update the previous position and time
                prev_position = position
                prev_time = datetime.now()

        else:
            # Update the previous position and time
            prev_position = position
            prev_time = datetime.now()

    # Average Speed and Save Average Speed
    avg_speed = sum(total_speed) / len(total_speed)
    rounded_avg_speed = round(avg_speed, ROUNDING_DECIMALS)

    # Save the average speed in the result file
    with open(RESULT_PATH, 'w') as result_file:
        result_file.write(f'{rounded_avg_speed}')
