# External module imports
import RPi.GPIO as GPIO
import time
# Pin Definitons:
ledPin = 23 #Broadcom pin 23
# Pin Setup:
# Broadcom pin-numbering scheme
GPIO.setmode(GPIO.BCM)
#set warning as false
GPIO.setwarnings(False)
# LED pin set as output
GPIO.setup(ledPin, GPIO.OUT) 
# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
            GPIO.output(ledPin, GPIO.HIGH)
            print("LED ON!!")
            time.sleep(0.5)
            GPIO.output(ledPin, GPIO.LOW)
            print("LED OFF!!")
            time.sleep(0.5)
# If CTRL+C is pressed, exit cleanly:
except KeyboardInterrupt:    
	GPIO.cleanup() # cleanup all GPIO
