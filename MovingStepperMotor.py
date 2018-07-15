#--- DO READ AND UNDERSTAND BEFORE RUNNING THE CODE ---
# This script have been reduce to it most simplest form in order to just to run the stepper motor, 
# Everything else like the DC motor control and the sensor check have been remove from this script,
# There are only 3 elements that are require to edit.
# Which are the pluseSwitch, numberOfPulse, and the direction. 
# The rest have been tested and confirm like for example the GPIO Setting and the Initial motor setting.

import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# --- Timmer setting --- (in Millisecond) [Editable]
pulseSwitch = 0.2  #pulse step delay in ms

# --- Number of Pulse --- [Editable]
numberOfPulse= 8600

# --- Direction of Movement --- (#Change Dir: HIGH is UP, LOW is DOWN) [Editable]
Direction = GPIO.HIGH
#Direction = GPIO.LOW

# --- GPIO Setting ---
MOVEena = 40
MOVEDir = 38
MOVEpal = 36

GPIO.setup(MOVEena,GPIO.OUT)
GPIO.setup(MOVEDir,GPIO.OUT)
GPIO.setup(MOVEpal,GPIO.OUT)

# --- The Pulse Function
def pulse(numberOfPulse,pulseSwitch):
	i = 0
	while i < numberOfPulse:
		GPIO.output(MOVEpal, GPIO.HIGH)
		time.sleep(pulseSwitch/1000)
		GPIO.output(MOVEpal, GPIO.LOW)
		time.sleep(pulseSwitch/1000)
		i = i + 1

# --- THE INITIAL MOTOR SETTING
GPIO.output(MOVEena, GPIO.HIGH)
time.sleep(0.05)
GPIO.output(MOVEDir, GPIO.HIGH)
time.sleep(0.05)
GPIO.output(MOVEpal, GPIO.LOW)

# --- Motor Movement Control ---
GPIO.output(MOVEena, GPIO.LOW)
time.sleep(0.05)
GPIO.output(MOVEDir, Direction) 
time.sleep(0.05)
pulse(numberOfPulse,pulseSwitch)
	
GPIO.output(MOVEena, GPIO.HIGH)	