#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import Float64, Bool,String

# Ce scirpt permet de communiquer avec une arduino, qui sera l'arduino de commande des moteurs
#
class serial_translator:
    
    def __init__(self):
        rospy.init_node('serial_translator', anonymous=True)

        #Publishers   
        self.pub_sensor = rospy.Publisher("/master/lidar", Bool, queue_size = 10)


        rospy.sleep(1)
        rospy.loginfo("[serial_translator] node started")

        #Subscribers
        rospy.Subscriber("/chatter", String, self.callback)
        rospy.Subscriber("/sensor/lidar", Bool, self.lidar_callback)


        rospy.spin()

       
    def callback(self,data):
        """
        when receive a topic [/card/<...>], publish the proper topic "/master/<...>"
        """
      
        try:
            rospy.loginfo("from arduino : %s",data.data)
        except rospy.ServiceException as e:
            rospy.logwarn("Service call failed: %s"%e)

    def lidar_callback(self,data):
        """
        when receive a topic [/card/<...>], publish the proper topic "/master/<...>"
        """
        rospy.loginfo("message receive from the sensor/lidar")
        self.pub_sensor.publish(data.data)           



if __name__ == '__main__':
    
    try:
        translate = serial_translator()
        
    except rospy.ROSInterruptException:
        pass
