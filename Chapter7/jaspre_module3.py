import re 
import paho.mqtt.subscribe as subscribe 
WORDS = ["TEMPERATURE", "HUMIDITY"] 
def handle(text, mic, profile): 
	broker_address="Raspberry Pi IP address" 
	topic = [’/feeds/temperature’] 
	print("temperture") 
	m = subscribe.simple(topic, 	hostname=broker_address, retained=False)
	msg = "It is " + m.payload + "degree celsius" 
	mic.say(msg) 

def isValid(text): 
	return bool(re.search(r’\bwhat is the 	temperature\b’, text, re.IGNORECASE)) 
