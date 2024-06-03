from machine import Pin, ADC
from time import sleep

adc_pin = Pin(4, Pin.IN)
moist = ADC(adc_pin)
moist.atten(ADC.ATTN_11DB)       #Full range: 3.3v

theor_max = 4095     # theoretical max value
theor_min = 0        # theoretical min value
sensor_max = 2550    # measured max value of sensor
sensor_min = 1170    # measured min value of sensor
calib = (theor_max - theor_min) / (sensor_max - sensor_min) # calibration factor
min=theor_max
max=theor_min

while True:
  raw_value = moist.read()
  if raw_value < min:
    min = raw_value
  if raw_value > max:
    max = raw_value
  calib_value =  (raw_value - sensor_min) * calib

  moisture = 1 - (calib_value / theor_max)

  # Limit moisture value between 0 and 1
  if (moisture > 1):
    moisture = 1
  elif (moisture < 0):
    moisture = 0

  # print(raw_value, "\nMin: ", min, "\nMax: ", max)
  # print("Calib. Value", calib_value)
  # print("Moisture: {0:.1%}".format(moisture))
  
  print("Moisture: {0:.1%} Raw values (current / min / max): {1: >4}/{2: >4}/{3: >4}".format(moisture, raw_value, min,max))
  sleep(2)