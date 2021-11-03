import RPi.GPIO as GPIO
import time
from PCF8591 import photores

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23]
LED = GPIO.setup(13, GPIO.OUT, initial=0) 

for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
             [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
        
state = 0  # current position in stator sequence

def delay_us(tus): 
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  # dir = +/- 1 (ccw / cw)
  state += dir
  if state > 7: state = 0
  elif state < 0: state =  7
  for pin in range(4):    # 4 pins that need to be energized
    GPIO.output(pins[pin], sequence[state][pin])
  delay_us(1000)

def moveSteps(steps, dir):
  for step in steps:
    halfstep(dir)

class stepper:
  def goangle(ang):
    gang = [0]
    nang = int(ang)*4000/360
    if gang+ang < 180:
      moveSteps(nang-gang[0], 1)
    else:
      moveSteps(nang-gang[0], -1)
    gang[0] = [ang]
  
  def zero():
    photor = photores(0x48)
    GPIO.HIGH(LED)
    if photor < 220:
      moveSteps(100, 1)
    else:
      GPIO.LOW(LED)

GPIO.cleanup() 