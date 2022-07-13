#/home/pi/Documents/home_automation/app.py
import Adafruit_DHT
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
 
app = Flask(__name__)
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led_bulb1 = 32
led_bulb2 = 36
 
# Define led pins as output
GPIO.setup(led_bulb1, GPIO.OUT)   
GPIO.setup(led_bulb2, GPIO.OUT) 
 
# Keep LEDs off in the beginning 
GPIO.output(led_bulb1, GPIO.LOW)
GPIO.output(led_bulb2, GPIO.LOW)
 
@app.route("/")
def index():
    # Check the current status of lights in the room
   
    return render_template('index.html')
     
@app.route("/<deviceName>/<action>",methods=['GET', 'POST'])
def action(deviceName, action):
   # temperature = ''
   # humidity = ''
    if deviceName == 'led_bulb1':
        device = led_bulb1
    if deviceName == 'led_bulb2':
        device = led_bulb2
    if action == "on":
        GPIO.output(device, GPIO.HIGH)
    if action == "off":
        GPIO.output(device, GPIO.LOW)
              
    led_bulb1_sts = GPIO.input(led_bulb1)
    led_bulb2_sts = GPIO.input(led_bulb2)
    humidity, temperature = Adafruit_DHT.read_retry(11, 21)
    templateData = {
        'led_bulb1'  : led_bulb1_sts,
        'led_bulb2'  : led_bulb2_sts,
        'humidity': humidity,
        'temperature' : temperature
    }
    return render_template('index.html', **templateData)
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
