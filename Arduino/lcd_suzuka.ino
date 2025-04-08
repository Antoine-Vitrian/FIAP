#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);


void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.begin(16, 2);

}

void loop() {
  lcd.setCursor(2,0);
  lcd.print("GP de Suzuka");
  delay(1000);
  lcd.setCursor(6,1);
  lcd.print("2025");

  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#1 Verstappen");
  lcd.setCursor(0,1);
  delay(1000);
  lcd.print("#4 Norris");
  
  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#81 Piastri");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("#16 Leclerc");
  
  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#63 Russell");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("#12 Antonelli");

  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#44 Hamilton");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("#7 Hadjar");

  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#23 Albon");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("#87 Bearman");

  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#14 Alonso");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("#22 Tsunoda");

  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#10 Gasly");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("#55 Sainz");

  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#15 Doohan");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("#27 Hulkenberg");

  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#30 Lawson");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("#31 Ocon");

  delay(1000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("#5 Bortoleto");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("#18 Stroll");

  delay(1000);
  lcd.clear();

  delay(2000);
}