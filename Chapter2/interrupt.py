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
#here define a function to be called when an interrupt occur, also turn on the LED inside

def my_callback(channel):  
	if GPIO.input(buttonPin):
		GPIO.output(ledPin, GPIO.HIGH)    
		print "Falling edge detected"  
	else:            
		GPIO.output(ledPin, GPIO.LOW)      
		print "Rising edge detected"  

#When a interrupt occur just call the above callback function whatever else is happening in the program
GPIO.add_event_detect(buttonPin, GPIO.BOTH, callback=my_callback) 

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
		print "Normal while loop is running"
# If CTRL+C is pressed, exit cleanly:
except KeyboardInterrupt:    
	GPIO.cleanup() # cleanup all GPIO
