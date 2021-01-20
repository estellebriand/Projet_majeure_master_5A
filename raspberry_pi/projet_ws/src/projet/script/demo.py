#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Int32, Bool
from sensor_msgs.msg import LaserScan
import numpy as np
import time
from projet.srv import Obstacle

class raspberry_publisher_demo():
    
    def __init__(self):

        self.obstacle=  False
        self.object_detected = ""
        rospy.init_node('raspberry_demo', anonymous=True)

        #pub = rospy.Publisher('/chatter', String, queue_size=10)
        #self.scan_pub = rospy.Publisher('/obstacle_spot', String, queue_size=10)
        #self.object_detected_pub = rospy.Publisher('/object_detected', String, queue_size=10)
        
        self.command_pub = rospy.Publisher('/command', Int32, queue_size=10) #command = stop - forward - turn_left - turn_right - bras_haut_ouvert - bras_haut_ferme - bras_bas_ouvert - bras_bas_ferme
               
        rospy.Subscriber('/obstacle', Bool, self.obstacle_update)

        rospy.wait_for_service('is_obstacle')
        rospy.loginfo("Node [raspberry_demo] started")
        time.sleep(10)
        rospy.loginfo("GO")
        '''
        while not rospy.is_shutdown(): 
            self.command_pub.publish(0)
            time.sleep(3)
        '''
        self.forward()
        time.sleep(8)
        self.stop()
        time.sleep(2)
        for i in range(0,10):
            self.turn("left")
            time.sleep(0.2)
        self.stop()
        time.sleep(2)
        self.forward()
        time.sleep(5)
        self.stop()
        time.sleep(2)
        
        rospy.spin()
    
    def obstacle_update(self,data):
        self.obstacle = data.data
        #if(data.data==True):
            #self.command_pub.publish(0)
            #rospy.loginfo("obstacle")
            #time.sleep(1)

    def forward(self):
        self.command_pub.publish(1)
    
    def stop(self):
        self.command_pub.publish(0)
    
    def turn(self,direction):
        if direction == "left":
            self.command_pub.publish(2)
        if direction == "right":
            self.command_pub.publish(3)        
    
    def grip(self):
        self.command_pub.publish(open_claw)
        time.sleep(6)   
        self.command_pub.publish(arm_down)
        time.sleep(2)        
        self.command_pub.publish(close_claw)
        self.command_pub.publish(arm_up)
        time.sleep(3)

if __name__ == '__main__':
    try:
        raspberry_publisher_demo()
    except rospy.ROSInterruptException:
        pass

