char commandValue; // данные, поступаемые с последовательного порта
int ledPin = 13; // встроенный светодиод
char but;
int data;
void setup() {
  pinMode(ledPin, OUTPUT); // режим на вывод данных
  Serial.begin(9600);
  but='0';
}

void loop() {
  if (Serial.available()) {
    commandValue = Serial.read();
  }

  if (commandValue == '1') {
    but=commandValue;
    digitalWrite(ledPin, HIGH); // включаем светодиод
      }
  if (commandValue == '0') {
    but=commandValue;
    digitalWrite(ledPin, LOW); // в противном случае выключаем
  }
  if (commandValue == '2') {
    if (but=='1'){
      data=123;
      }
    if (but=='0'){
      data=100;
      }
    Serial.print('x');
    Serial.println(data);
   }
  commandValue='x';
 // задержка перед следующим чтением данных
}