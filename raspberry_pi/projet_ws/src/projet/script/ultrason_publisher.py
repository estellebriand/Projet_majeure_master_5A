#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64, Bool
import RPi.GPIO as GPIO
import time

from projet.srv import Obstacle

#source code: https://raspberry-lab.fr/Composants/Mesure-de-distance-avec-HC-SR04-Raspberry-Francais/
#Update: Estelle Briand
#Date: 15/01/2021
#Code to detect the distance with the HC-SR04 sensor and a RaspberryPi
#WorldSkills robot project 

class ultrason_publisher():
    def __init__(self):
        self.command = False
        rospy.init_node('raspberry_ulstrason_publisher', anonymous=True)
        self.ultrason_pub = rospy.Publisher('/ultrason', Int64, queue_size=10)
        self.obstacle_pub = rospy.Publisher('/obstacle', Bool, queue_size=10)

        s = rospy.Service('is_obstacle', Obstacle, self.handle_is_obstacle)
        GPIO.setmode(GPIO.BCM)

        self.Trig = 23          # Entree Trig du HC-SR04 branchee au GPIO 23
        self.Echo = 24         # Sortie Echo du HC-SR04 branchee au GPIO 24
        

        GPIO.setup(self.Trig,GPIO.OUT)
        GPIO.setup(self.Echo,GPIO.IN)

        GPIO.output(self.Trig, False)
        rospy.loginfo("Node [raspberry_ultrason_publisher] started")
        rate = rospy.Rate(50)
        
        while not rospy.is_shutdown(): 
            self.process()
            rate.sleep()

        GPIO.cleanup()
    
    def handle_is_obstacle(self,req):
        return self.command

    def process(self):
        time.sleep(1)       # On la prend toute les 1 seconde

        GPIO.output(self.Trig, True)
        time.sleep(0.00001)
        GPIO.output(self.Trig, False)

        while GPIO.input(self.Echo)==0:  ## Emission de l'ultrason
            debutImpulsion = time.time()

        while GPIO.input(self.Echo)==1:   ## Retour de l'Echo
            finImpulsion = time.time()

        distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s

        msg = distance 
        self.command = False

        if distance < 30: 
            self.command = True
        else:
            self.command = False

        self.obstacle_pub.publish(self.command)  
                    
        self.ultrason_pub.publish(msg)     

if __name__ == '__main__':
    try:
        ultrason_publisher()
    except rospy.ROSInterruptException:
        pass

