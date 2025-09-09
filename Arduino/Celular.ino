#define led 13
#define trigger 8
#define echo 7
int dist = 0;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
}

void loop() {
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo, HIGH);
  Serial.println(dist);

  if(Serial.available() > 0){
    char comando = Serial.read();
    if(comando == '1'){
      digitalWrite(led, HIGH);
    }
    else if(comando == '0'){
      digitalWrite(led, LOW);
    }
  }
}