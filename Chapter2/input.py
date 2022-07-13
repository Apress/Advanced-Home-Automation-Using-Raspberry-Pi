# External module imports
import RPi.GPIO as GPIO
import time
# Pin Definition:
ledPin = 23 #Broadcom pin 23
buttonPin = 20 
# Pin Setup:
# Broadcom pin-numbering scheme
GPIO.setmode(GPIO.BCM)
#set warning as false
GPIO.setwarnings(False)
# LED pin set as output 
GPIO.setup(ledPin, GPIO.OUT) 
#button pin input with pull-up
GPIO.setup(buttonPin, GPIO.IN,pull_up_down = GPIO.PUD_UP) 

# Initial state for LED:
GPIO.output(ledPin, GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
		 buttonValue = GPIO.input(buttonPin)
#when button is pressed it will give 0
		 if (buttonValue == false)
            	GPIO.output(ledPin, GPIO.HIGH)
            	print("Button pressed & LED ON!!")
            	time.sleep(0.5)
           else
			GPIO.output(ledPin, GPIO.LOW)
# If CTRL+C is pressed, exit cleanly:
except KeyboardInterrupt:    
	GPIO.cleanup() # cleanup all GPIO
