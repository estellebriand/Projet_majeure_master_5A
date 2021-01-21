#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import numpy as np


class raspberry_publisher():
    
    def __init__(self):

        self.obstacles_spot=  ""
        self.object_detected = ""
        rospy.init_node('raspberry_publisher', anonymous=True)

        #pub = rospy.Publisher('/chatter', String, queue_size=10)
        scan_pub = rospy.Publisher('/obstacle_spot', String, queue_size=10)
        self.object_detected_pub = rospy.Publisher('/object_detected', String, queue_size=10)

        rate = rospy.Rate(2) # 10hz
        
        rospy.Subscriber('/scan', LaserScan, self.laserscan)
        rate.sleep()
        #rospy.wait_for_message('/scan')
        rospy.loginfo("Node [raspberry_publisher] started")
        
        while not rospy.is_shutdown():
            scan_pub.publish(self.obstacles_spot)
            self.detection()
            rate.sleep()

    def test(self):
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            #rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()

    def laserscan(self,data):
        ranges = data.ranges
        obstacles= { "devant":False,"derriere":False,"gauche":False,"droite":False}
       
        for p in range(0, len(ranges)):
            # Front position
            if (p >= 0 and p < 70) or (p > 290 and p<=360): # 315<p<360 or 0<p<45
              #remove infinite value
              if ranges[p] != np.inf and ranges[p] < 0.20:
                    # if we get value <0.2 we have an obstacle
                    obstacles["devant"] = True
            
            # right position
            if (p < 290 and p>=225): # 225<p<315
                #remove infinite value
                if ranges[p] != np.inf and ranges[p] < 0.30:
                    # if we get value <0.2 we have an obstacle
                    obstacles["droite"] = True
   
            # Back position
            if (p < 225 and p>=135): # 135<p<225
                #remove infinite value
                if ranges[p] != np.inf and ranges[p] < 0.30:
                    # if we get value <0.2 we have an obstacle
                    obstacles["derriere"] = True
            # Left position
            if (p < 135 and p>=70):
                #remove infinite value
                if ranges[p] != np.inf and ranges[p] < 0.30:
                    # if we get value <0.1 we have an obstacle
                    obstacles["gauche"] = True

        self.obstacles_spot = "devant " + str(obstacles["devant"]) +",derriere " + str(obstacles["derriere"]) +",droite " + str(obstacles["droite"]) +",gauche " + str(obstacles["gauche"])
        return

    def detection(self):
        self.object_detected= "Cannette x y"
        self.object_detected_pub.publish(self.object_detected)


if __name__ == '__main__':
    try:
        raspberry_publisher()
    except rospy.ROSInterruptException:
        pass

