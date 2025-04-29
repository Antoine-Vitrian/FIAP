#include <Servo.h>
int dist = 0;
#define servoPin 3
#define led01 4
#define trigger 8
#define echo 7

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  pinMode(led01, OUTPUT);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
}

void loop() {
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo, HIGH);
  dist = dist/58;

  Serial.println("Distância é igual a " + String(dist) +"cm");

  if(dist < 200){
    digitalWrite(led01, HIGH);
    myServo.write(180);
  }
  else{
    digitalWrite(led01, LOW);
    myServo.write(0);
  }
}