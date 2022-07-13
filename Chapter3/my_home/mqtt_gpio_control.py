import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import  time
broker_ip="raspberry_pi_IP_address"
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,0)
GPIO.setwarnings(False)
print("value is ",GPIO.input(18))

def on_message(client, userdata, message):
   m=str(message.payload.decode("utf-8"))
   topic=message.topic
   messages.append([topic,m])
   
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        client.subscribe(sub_topic)
    else:
        client.bad_connection_flag=True
        client.connected_flag=False

#MQTT SETUP
messages=[]
sub_topic="pi/GPIO/control/#"
client= mqtt.Client()  
client.on_message=on_message
client.on_connect=on_connect
client.connected_flag=False
client.connect(broker_ip)
while True:
    client.loop(0.01)
    time.sleep(1)
    if len(messages)>0:
        m=messages.pop(0)
        print("received ",m)
        GPIO.output(18,int(m[1]))
