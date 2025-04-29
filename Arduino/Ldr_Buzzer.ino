#define green 13
#define yellow 12
#define red 11
#define buzzer 2
#define ldr A0
float ldrValor = 0;

void setup() {
  Serial.begin(9600);
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(ldr, INPUT);
}

void loop() {
  ldrValor = analogRead(ldr)

  Serial.println(ldrValor);
  if(ldrValor < 200){
    digitalWrite(green, HIGH);
    digitalWrite(yellow, LOW);
    digitalWrite(red, LOW);
  }
  else if(ldrValor < 400){
    digitalWrite(green, LOW);
    digitalWrite(yellow, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(buzzer, HIGH);
    delay(3000);
    digitalWrite(buzzer, LOW);
  }
  else{
    digitalWrite(green, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(red, HIGH);
  } 
}