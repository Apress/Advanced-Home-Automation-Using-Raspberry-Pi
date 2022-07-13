#include <ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include "DHT.h"

/************************* Pin Definition *********************************/

//Relays for switching appliances
#define LED            D5


//DHT11 for reading temperature and humidity value
#define DHTPIN            D4


/************************* WiFi Access Point *********************************/

#define WLAN_SSID       "awesome"
#define WLAN_PASS       "awesome12"

/************************* Adafruit.io Setup *********************************/

#define AIO_SERVER      "192.168.43.177" //IP address of RPi
#define AIO_SERVERPORT  1883                   // use 8883 for SSL
#define AIO_USERNAME    ""
#define AIO_KEY         ""

/************ Global State (you don't need to change this!) ******************/

// Create an ESP8266 WiFiClient class to connect to the MQTT server.
WiFiClient client;
// or... use WiFiFlientSecure for SSL
//WiFiClientSecure client;

// Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);

/****************************** Feeds ***************************************/

// Notice MQTT paths for AIO follow the form: <username>/feeds/<feedname>
Adafruit_MQTT_Publish Temperature = Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/temperature");

// Setup a feed called 'onoff' for subscribing to changes.
Adafruit_MQTT_Subscribe led1 = Adafruit_MQTT_Subscribe(&mqtt, AIO_USERNAME "/feeds/led");




/************ Necessary declaration for DHT11 ******************/
#define DHTTYPE           DHT11     // DHT 11 

DHT dht(DHTPIN, DHTTYPE);
uint32_t delayMS;


/*************************** Sketch Code ************************************/

// Bug workaround for Arduino 1.6.6, it seems to need a function declaration
// for some reason (only affects ESP8266, likely an arduino-builder bug).
void MQTT_connect();
//Servo myservo;
void setup() {
  Serial.begin(115200);

  delay(10);
  pinMode(LED, OUTPUT);
  Serial.println(F("Adafruit MQTT demo"));

  // Connect to WiFi access point.
  Serial.println(); Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.println("WiFi connected");
  Serial.println("IP address: "); Serial.println(WiFi.localIP());
  
  //Setting up DHT sensor
  dht.begin();

  // Setup MQTT subscription for onoff feed.
  mqtt.subscribe(&led1);
 
}

uint32_t x = 0;

void loop() {
  // Ensure the connection to the MQTT server is alive (this will make the first
  // connection and automatically reconnect when disconnected).  See the MQTT_connect
  // function definition further below.
  MQTT_connect();
  // this is our 'wait for incoming subscription packets' busy subloop
  // try to spend your time here

  Adafruit_MQTT_Subscribe *subscription;
  while ((subscription = mqtt.readSubscription(20000))) {
    if (subscription == &led1) {
      Serial.print(F("Got: "));
      Serial.println((char *)led1.lastread);
      int led1_State = atoi((char *)led1.lastread);
      digitalWrite(LED, led1_State);
      Serial.println("onnn");
    }
   
  }

  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Check if any reads failed and exit early (to try again).
  if (isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  if (! Temperature.publish(t)) {
    Serial.println(F("Failed"));
  } else {
    Serial.println(F("OK!"));
  }

}

// Function to connect and reconnect as necessary to the MQTT server.
// Should be called in the loop function and it will take care if connecting.
void MQTT_connect() {
  int8_t ret;

  // Stop if already connected.
  if (mqtt.connected()) {
    return;
  }

  Serial.print("Connecting to MQTT... ");

  uint8_t retries = 3;
  while ((ret = mqtt.connect()) != 0) { // connect will return 0 for connected
    Serial.println(mqtt.connectErrorString(ret));
    Serial.println("Retrying MQTT connection in 5 seconds...");
    mqtt.disconnect();
    delay(5000);  // wait 5 seconds
    retries--;
    if (retries == 0) {
      // basically die and wait for WDT to reset me
      while (1);
    }
  }
  Serial.println("MQTT Connected!");
}
