#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <DHT.h>
#include <BlynkSimpleEsp8266.h>

#define DHTPIN 5          
#define DHTTYPE DHT11     
DHT dht(DHTPIN, DHTTYPE);
char auth[] = "Received Token id ";
char ssid[] = "Your WiFi name";
char pass[] = "WiFi password";
BlynkTimer timer;
void sendSensor(){
  float t = dht.readTemperature(); 
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;}
  Blynk.virtualWrite(V6, t);
}
void setup()
{
    Serial.begin(9600);
  dht.begin();
  Blynk.begin(auth, ssid, pass, IPAddress(192,168,1,20), 8080);
 timer.setInterval(1000L, sendSensor);
}
void loop()
{
  Blynk.run();
  timer.run();
}
