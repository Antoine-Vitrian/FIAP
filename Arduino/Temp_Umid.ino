#include<DHT.h>

#define dhtPin 2
#define dhtType DHT11
#define red 3
#define yellow 4
#define green 5

DHT dht(dhtPin, dhtType);

void setup() {
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
  Serial.begin(9600);
  dht.begin();

}

void loop() {
  int temperatura = dht.readTemperature();
  int umidade = dht.readHumidity();

  Serial.println("Temperatura: " + String(temperatura));
  Serial.println("Umidade: " + String(umidade));
  delay(2000);

  if (temperatura = 26 && umidade > 20){
    digitalWrite(red, HIGH);
    digitalWrite(yellow, LOW);
    digitalWrite(green, LOW);
  }
  else{
    digitalWrite(red, LOW);
    digitalWrite(yellow, HIGH);
    digitalWrite(green, LOW);
  }
}