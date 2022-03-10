# File: sonar.py
# necessario importare sys, altrimenti non esegue: sys.stdout.flush()
import sys

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 4
ECHO = 17

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# TRIG parte LOW
GPIO.output(TRIG, False)

print ('Waiting a few seconds for the sensor to settle')
time.sleep(2)
try:
     while True:
         # invia impulsoTRIG
         GPIO.output(TRIG, True)
         time.sleep(0.00001)
         GPIO.output(TRIG, False)

# attendi che ECHO parta e memorizza tempo
         while GPIO.input(ECHO) == 0:
              pulse_start = time.time()

# register the last timestamp at which the receiver detects the signal.
         while GPIO.input(ECHO) == 1:
              pulse_end = time.time()

         pulse_duration = pulse_end - pulse_start
         # distance = vt/2
         distance = (pulse_duration * 34330)/2
         distance = round(distance, 1)

# print ('Distance:',distance,'cm')
         print (distance)
# Importante: forza a scrivere quanto presente nel buffer senza ritardo
         sys.stdout.flush()
         time.sleep(0.25)

except KeyboardInterrupt:
    GPIO.cleanup()
