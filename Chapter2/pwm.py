# External module imports
import RPi.GPIO as GPIO
import time

# Pin Setup:
# Broadcom pin-numbering scheme
GPIO.setmode(GPIO.BCM) 
# Set GPIO pin 18 to output mode.
GPIO.setup(18, GPIO.OUT) 
 
# Initialize PWM on pwmPin 100Hz frequency
pwm = GPIO.PWM(18, 100)   
print("Here we go! Press CTRL+C to exit")
# set dc variable to 0 for 0%
duty_cycle=0 
# Start PWM with 0% duty cycle                              pwm.start(duty_cycle) 
                     
try:
  while True:  
# Loop 0 to 100 stepping dc by 5 each loop                    
    for duty_cycle in range(0, 101, 5):          		pwm.ChangeDutyCycle(duty_cycle)
	time.sleep(0.5)                   	print(duty_cycle)
# Loop 95 to 5 stepping dc down by 5 each loop
    for duty_cycle in range(95, 0, -5):          	pwm.ChangeDutyCycle(duty_cycle)
    	time.sleep(0.5)                   	print(duty_cycle)
# If CTRL+C is pressed, exit cleanly:
except KeyboardInterrupt:    
	pwm.stop()              # stop PWM
    	GPIO.cleanup() 	# cleanup all GPIO
