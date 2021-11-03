from urllib.request import urlopen
from urllib.parse import urlencode
from stp import stepper

import RPi.GPIO as GPIO
import time
import json

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23]
LED = GPIO.setup(13, GPIO.OUT, initial=0) 

for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

api = "KSPTXP4NN3FAJOW3"

while True:
  with open("stpstor.txt", 'r') as f:
    data = json.load(f)
    angle = str(data['angle'])
    sangle = str(data['subangle'])
    zangle = str(data['zangle'])
    stp = stepper

    if sangle == 'Angle Input':
      stp.goangle(angle)
    
    if zangle == 'Zero Angle':
      stp.zero()
    
    params = {"api_key":api, 1:angle}
    params = urlencode(params)
    response = urlopen("https://api.thingspeak.com/update?" + params)

GPIO.cleanup()