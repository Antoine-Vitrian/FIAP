#include <Servo.h>
#define servoPin 3

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
}

void loop() {
  myServo.write(90);
  delay(1000);
  myServo.write(45);
  delay(1000);
  myServo.write(120);
  delay(1000);
  myServo.write(30);
  delay(1000);
  myServo.write(180);
  delay(1000);
  myServo.write(0);
  delay(1000);
}