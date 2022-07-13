import paho.mqtt.publish as publish 
import re 
DEVICES = ["FAN","LIGHT", "LIGHTS"] 
PAYLOADS = ["ON","OFF"] 
ROOMS = ["BEDROOM","LIVINGROOM","DRAWINGROOM"
EXTRAS = ["THE","THAT"] 
STARTS = ["SWITCH", "TURN"] 
WORDS = STARTS + DEVICES + EXTRAS + PAYLOADS + ROOMS 
PRIORITY = 4 
def handle(text, mic, profile): 
	words = text.split(’ ’) 
	payload = words[1] 
	device = words[4] 
	room = words[3] 
	if words[4] not in DEVICES: 
		return mic.say(words[4]+" not found in the 		list of devices") 
	print("payload->"+payload) 
	print("Device ->"+device) 
	print("Room ->" +room) 
	top = [ room, device, payload] 
	topic = ’/’.join([’/feeds’]+top) 
	publish.single(topic.lower(),payload=payload.lo	wer(),hostname="Raspberry pi IP address")
	print(topic.lower()) 
	mic.say("Done")
def isValid(text): 
	regex = "(" + "|".join(STARTS) + ") ("+ 	"|".join(PAYLOADS) + ") (" + "|".joinreturn 	bool(re.search(regex, text, re.IGNORECASE)) 
