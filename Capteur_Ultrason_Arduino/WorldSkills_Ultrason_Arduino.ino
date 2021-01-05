/*
Mesure de distance à l'aide d'un capteur HC-SR04 et d'un Arduino
Projets Robotique fin de majeure robotique CPE Lyon - Nicolas Guy 
Circuit - repérage des broches
- VCC avec la broche 5V de l'Arduino
- GND avec la broche GND de l'Arduino
- Trig avec la broche 2 de l'Arduino
- Echo avec la broche 3 de l'Arduino

Librairie: HCSR04 by Martin Sosic
*/

#include <HCSR04.h>

// defines pins numbers / definition des broches du capteur
const int trigPin = 2;
const int echoPin = 3;
 
// Initialize sensor that uses digital pins trigPin and echoPin / initialisation du capteur avec les broches utilisees.
UltraSonicDistanceSensor distanceSensor(trigPin, echoPin);
void setup() {
  // We initialize serial connection so that we could print values from sensor./ initialisation du port serie a 9600 band pour afficher les valeurs mesurees par le capteur.
  Serial.begin(9600); 
}
void loop() {
  // Every 500 miliseconds, do a measurement using the sensor and print the distance in centimeters./ toutes les 500 millisecondes nous faisons une mesure et nous affichons la distance en centimetre sur le port serie.
  Serial.println(distanceSensor.measureDistanceCm());
  delay(500);
}
