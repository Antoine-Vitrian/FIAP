#define trigger 
#define echo 

dist = 0;
int red = 6;
int yellow = 5;
int green = 4;

void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);

  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo, HIGH);
  dist = dist/58;

  Serial.println("Distância é igual a " + String(dist) +"cm");

  if(dist < 50){
    digitalWrite(red, HIGH)
    digitalWrite(yellow, LOW)
    digitalWrite(green, LOW)
  }
  else if(dist < 120){
    digitalWrite(red, LOW)
    digitalWrite(yellow, HIGH)
    digitalWrite(green, LOW)
  }
  else{
    digitalWrite(red, LOW)
    digitalWrite(yellow, LOW)
    digitalWrite(green, HIGH)
  }
}