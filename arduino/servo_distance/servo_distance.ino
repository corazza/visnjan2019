#include <Servo.h>

#define echoPin 7
#define trigPin 8
#define servoPin 9
#define MAX_DISTANCE 30
#define MAX_ANGLE 50

Servo myservo;
int last_pos = 0;

void setup() {
  Serial.begin(9600);
  myservo.attach(servoPin);
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
}

void loop() {  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  int duration = pulseIn(echoPin, HIGH);

  int distance = duration/58.2;

  float a = distance > MAX_DISTANCE ? MAX_DISTANCE : distance;
  a = a < 0 ? 0 : a;
  int pos = abs(MAX_ANGLE * (a / MAX_DISTANCE));

  if (abs(pos - last_pos) < 10) myservo.write(60+pos);

  Serial.print("distance: ");
  Serial.print(distance);
  Serial.print(", a: ");
  Serial.print(a);
  Serial.print(", pos: ");
  Serial.print(pos);
  Serial.print(", last_pos: ");
  Serial.print(last_pos);
  Serial.println();

  last_pos = pos;
  
  delay(50);
}
