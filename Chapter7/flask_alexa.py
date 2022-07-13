from flask import Flask
from flask_ask import Ask, statement
import RPi.GPIO as GPIO
app = Flask(__name__)
ask = Ask(app, '/')
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
red_led = 18
white_led = 32
blue_led = 36
# Define led pins as output
GPIO.setup(red_led, GPIO.OUT)   
GPIO.setup(white_led, GPIO.OUT) 
GPIO.setup(blue_led, GPIO.OUT)
# Keep LEDs off in the beginning 
GPIO.output(red_led, GPIO.LOW)
GPIO.output(white_led, GPIO.LOW)
GPIO.output(blue_led, GPIO.LOW)
@ask.intent('LedIntent')
def led(color, status):
  if color.lower() not in pins.keys():
    return statement("Sorry {} color not supported".format(color)) 
  GPIO.output(pins[color], GPIO.HIGH if status == 'on' else GPIO.LOW)
  return statement('Turning {} light {}'.format(color, status))
if __name__ == '__main__':
  try:
    app.run(debug=True)
  finally:
    GPIO.cleanup()
