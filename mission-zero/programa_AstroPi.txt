from sense_hat import SenseHat
import time
from time import sleep
sense = SenseHat()
sense.set_rotation(270)
sense.color.gain = 60
sense.color.integration_cycles = 64
tiempo_ini = time.time()
print(tiempo_ini)

tiempo_ini = time.time()
tiempo = 0
tiempo_trans = 0

while tiempo_trans < 30:
  tiempo = time.time()
  tiempo_trans = tiempo - tiempo_ini
  print(tiempo_trans)

  sleep(2 * sense.colour.integration_time)
  red, green, blue, clear = sense.colour.colour # readings scaled to 0-256
  
  R = [255, 0, 0]  # Red
  B = [0, 0, 0]  # Black
  O = [255, 150, 0] #Orange
  W = [255, 255, 255] #White
  A = [red, green, blue] #Azul

  temp = sense.get_temperature()
  hum = sense.get_humidity()
  #print("Temperature: %s C" % temp)
  #print("Humidity: %s C" % hum)
  
  if temp < 30:
    question_mark = [
    A, A, A, A, A, A, A, A,
    A, W, W, W, A, A, A, A,
    A, B, W, W, A, A, A, A,
    O, W, W, W, A, A, W, A,
    A, A, W, W, W, W, W, A,
    A, A, W, W, W, W, W, A,
    A, A, W, W, W, W, W, A,
    A, A, A, O, A, O, A, A
    ]
    sense.set_pixels(question_mark)
  else:
    if temp < 100:
      question_mark = [
      A, A, A, A, A, A, A, A,
      A, R, R, R, A, A, A, A,
      A, W, R, R, A, A, A, A,
      O, R, R, R, A, A, R, A,
      A, A, R, R, R, R, R, A,
      A, A, R, R, R, R, R, A,
      A, A, R, R, R, R, R, A,
      A, A, A, O, A, O, A, A
      ]
      sense.set_pixels(question_mark)
    else:
      question_mark = [
      A, A, A, A, A, A, A, A,
      A, B, B, B, A, A, A, A,
      A, R, B, B, A, A, A, A,
      O, B, B, B, A, A, B, A,
      A, A, B, B, B, B, B, A,
      A, A, B, B, B, B, B, A,
      A, A, B, B, B, B, B, A,
      A, A, A, O, A, O, A, A
      ]
      sense.set_pixels(question_mark)
