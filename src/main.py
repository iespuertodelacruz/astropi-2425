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

from datetime import datetime, timedelta

from sense_hat import SenseHat

from utils import calculate_speed, get_ISS_position

# ==============================================================================

OUT_PATH = 'iss_matraka.csv'
SPEED_LOG_PATH = 'speed_log.csv'
RESULT_PATH = 'result.txt'
DURATION_MINUTES = 9
INTERVAL = 10
ROUNDING_DECIMALS = 4
HEADER = [
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
]

sense = SenseHat()
# ==============================================================================


with open(OUT_PATH, 'w') as f, open(SPEED_LOG_PATH, 'w') as speed_log:
    f.write(','.join(HEADER) + '\n')
    speed_log.write('date_time_utc,speed_km_s\n')

    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=DURATION_MINUTES)

    prev_position = None
    prev_time = None
    total_speed = []

    while datetime.now() < end_time:
        timestamp = datetime.now().isoformat()
        position = get_ISS_position()

        # 10 Second Interval for Saving Data
        if prev_position is not None and prev_time is not None:
            time_diff = (datetime.now() - prev_time).total_seconds()
            if time_diff >= INTERVAL:
                # Speeds and Save Speeds
                speed = calculate_speed(
                    (prev_position['latitude'], prev_position['longitude']),
                    (position['latitude'], position['longitude']),
                    time_diff,
                )
                total_speed.append(speed)

                rounded_speed = round(speed, ROUNDING_DECIMALS)
                speed_log.write(f'{timestamp},{rounded_speed}\n')
                speed_log.flush()

                # Other Measurements and Save Measurements
                temperature = sense.get_temperature()
                humidity = sense.get_humidity()
                pressure = sense.get_pressure()
                sense.set_imu_config(compass_enabled=True, gyro_enabled=False, accel_enabled=False)
                magnetic = sense.get_compass_raw()
                sense.set_imu_config(compass_enabled=False, gyro_enabled=True, accel_enabled=False)
                rotation = sense.get_gyroscope_raw()
                sense.set_imu_config(compass_enabled=False, gyro_enabled=False, accel_enabled=True)
                acceleration = sense.get_accelerometer_raw()

                f.write(
                    f'{timestamp},{position["latitude"]},{position["longitude"]},{temperature},'
                    f'{humidity},{pressure},{magnetic["x"]},{magnetic["y"]},{magnetic["z"]},'
                    f'{acceleration["x"]},{acceleration["y"]},{acceleration["z"]},'
                    f'{rotation["x"]},{rotation["y"]},{rotation["z"]},{rounded_speed}\n'
                )
                f.flush()

                prev_position = position
                prev_time = datetime.now()

        else:
            prev_position = position
            prev_time = datetime.now()

    # Average Speed ​​and Save Average Speed
    avg_speed = sum(total_speed) / len(total_speed)
    rounded_avg_speed = round(avg_speed, ROUNDING_DECIMALS)
    with open(RESULT_PATH, 'w') as result_file:
        result_file.write(f'{rounded_avg_speed}')
