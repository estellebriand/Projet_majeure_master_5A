import RPi.GPIO as GPIO
import time

#source code: https://raspberry-lab.fr/Composants/Mesure-de-distance-avec-HC-SR04-Raspberry-Francais/
#Update: Nicolas Guy
#Date: 04/01/2021
#Code to detect the distance with the HC-SR04 sensor and a RaspberryPi
#WorldSkills robot project 

GPIO.setmode(GPIO.BCM)

print ("+-----------------------------------------------------------+")
print ("|   Mesure de distance par le capteur ultrasonore HC-SR04   |")
print ("+-----------------------------------------------------------+")

Trig = 23          # Entree Trig du HC-SR04 branchee au GPIO 23
Echo = 24         # Sortie Echo du HC-SR04 branchee au GPIO 24

GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

GPIO.output(Trig, False)

repet = input("Entrez un nombre de repetitions de mesure : ")
repet = int(repet)

for x in range(repet):    # On prend la mesure "repet" fois

   time.sleep(1)       # On la prend toute les 1 seconde

   GPIO.output(Trig, True)
   time.sleep(0.00001)
   GPIO.output(Trig, False)

   while GPIO.input(Echo)==0:  ## Emission de l'ultrason
     debutImpulsion = time.time()

   while GPIO.input(Echo)==1:   ## Retour de l'Echo
     finImpulsion = time.time()

   distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s

   print ("La distance est de : ",distance," cm")

GPIO.cleanup()
