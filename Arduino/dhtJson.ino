#include<ArduinoJson.h>
#include<DHT.h>

#define dhttype 11
#define dhtpin 7
DHT dht(dhtpin, dhttype);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  int temp = dht.readTemperature();
  int umi = dht.readHumidity();

  // Criando documento JSON <Tamanho em bytes> nome_do_doc
  StaticJsonDocument<100>json;

  // Criando atributo Json
  json["Temperature"] = temp;
  json["Humidity"] = umi;

  serializeJson(json, Serial);

  Serial.println();

}