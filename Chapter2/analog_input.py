#Importing modules
# To communicate with SPI devices
import spidev 
from time import sleep

pot_channel = 0
# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0) 

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Below function will convert data to voltage
def Volts(data):
  volts = (data * 3.3) / float(1023)
# Round off to 2 decimal places
  volts = round(volts, 2)
  return volts
 
while True:
# Reading from CH0
  temp_output = analogInput(pot_channel)
  temp_volts = Volts(temp_output)   
  print("ADC Value: ".format(temp_output))                                                                                      
  print("Voltage: ".format(temp_volts))
  sleep(1)
