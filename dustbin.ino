#include <Servo.h>

const int TRIG_PIN = 6;             // The SONAR trigger PIN
const int ECHO_PIN = 7;             // The SONAR echo PIN
const int SERVO_PIN = 9;            // The Servo motor PIN
const int DISTANCE_THRESHOLD = 20;  // Threshold distance (in centimeters) between object and dustbin
const int AUTO_CLOSE_TIME = 5000;   // Auto close time of the lid (in milliseconds)

Servo servo;

float duration_us, distance_cm;     // duration in microseconds, distance in centimeters

unsigned long openTime;             // time for which the lid is open
bool isOpen = false;                // whether the lid is open or not

void setup() {
    Serial.begin(9600);
    pinMode(TRIG_PIN, OUTPUT);      // Make trigger pin as output
    pinMode(ECHO_PIN, INPUT);       // Make echo pin as inut
    servo.attach(SERVO_PIN);        // attach the servo
    servo.write(0);                 // reset the servo back to 0deg
}

void loop() {
    // Sends a signal to the trigger pin for 10 microseconds
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    // Calculate the distance between the object and SONAR
    duration_us = pulseIn(ECHO_PIN, HIGH);
    distance_cm = 0.017 * duration_us;

    if (distance_cm < DISTANCE_THRESHOLD) {
        if (!isOpen) {
            isOpen = true;
            servo.write(180);
            openTime = millis();
        }
    }
//    } else {
//        if (isOpen) {
//            isOpen = false;
//            servo.write(0);
//            openTime = 0;
//        }
//    }

    if (isOpen) {
        if (millis() - openTime > AUTO_CLOSE_TIME) {
            isOpen = false;
            servo.write(0);
            openTime = 0;
        }
    }
    
    delay(500);
}
