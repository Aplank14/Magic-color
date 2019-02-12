import RPi.GPIO as GPIO
import time

#Function to turn the red led on
def redOn():
    GPIO.output(20, GPIO.HIGH)
    return
i
#Function to turn the green led on
def greenOn():
    GPIO.output(26, GPIO.HIGH)
    return

#Function to turn the blue led on
def blueOn():
    GPIO.output(21, GPIO.HIGH)
    return

#Function to turn all the leds off
def allOff():
    GPIO.output(21,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    return  

#Initial setup, don't touch
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

##Write your code below!##

