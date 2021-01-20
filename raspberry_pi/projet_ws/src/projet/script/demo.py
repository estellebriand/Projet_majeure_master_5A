#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import numpy as np
import time

class raspberry_publisher():
    
    def __init__(self):

        self.obstacles_spot=  ""
        self.object_detected = ""
        rospy.init_node('raspberry_demo', anonymous=True)

        #pub = rospy.Publisher('/chatter', String, queue_size=10)
        #self.scan_pub = rospy.Publisher('/obstacle_spot', String, queue_size=10)
        #self.object_detected_pub = rospy.Publisher('/object_detected', String, queue_size=10)
        
        self.command_pub = rospy.Publisher('/command', String, queue_size=10) #command = Stop - Forward - Turn_left - Turn_right - Arm_up - Arm_down - Open_claw - Close_claw
        
        rate = rospy.Rate(2) # 10hz
        
        #rospy.Subscriber('/scan', LaserScan, self.laserscan)

        rate.sleep()
        #rospy.wait_for_message('/scan')
        rospy.loginfo("Node [raspberry_demo] started")
        


    def forward(self, dist):
        #le motor tourne 50 __
        time_process = 50 * dist
        
        while timing < time_process:
            self.command_pub("Forward")

    def turn(direction):
        if direction == "right":
            self.command_pub("Turn_right")
        elif direction == "left":
            self.command_pub("Turn_left")
    
    def stop(self):
        self.command_pub("stop")

    def grip(self):
        self.command_pub(Open_claw)
        time.sleep(6000)   
        self.command_pub(Arm_down)
        time.sleep(2000)        
        self.command_pub(Close_claw)
        self.command_pub(Arm_up)
        time.sleep(300)

if __name__ == '__main__':
    try:
        raspberry_publisher()
    except rospy.ROSInterruptException:
        pass

