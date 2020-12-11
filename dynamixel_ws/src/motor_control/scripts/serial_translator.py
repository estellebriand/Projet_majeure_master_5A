#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import Float64, Bool,String


class serial_translator:
    
    def __init__(self):
        rospy.init_node('serial_translator', anonymous=True)

        #Publishers   
        self.pub_sensor = rospy.Publisher("/master/fake_sensor", Bool, queue_size = 10)


        rospy.sleep(1)
        rospy.loginfo("[serial_translator] node started")

        #Subscribers
        rospy.Subscriber("/chatter", String, self.callback)
        rospy.Subscriber("/sensor/fake_lidar", Bool, self.sensor_callback)


        rospy.spin()

       
    def callback(self,data):
        """
        when receive a topic [/card/<...>], publish the proper topic "/master/<...>"
        """
      
        try:
            rospy.loginfo("from ESP32 : %s",data.data)
        except rospy.ServiceException as e:
            rospy.logwarn("Service call failed: %s"%e)

    def sensor_callback(self,data):
        """
        when receive a topic [/card/<...>], publish the proper topic "/master/<...>"
        """
        rospy.loginfo("message receive from the sensor/sake_sensor")
        self.pub_sensor.publish(data.data)           



if __name__ == '__main__':
    
    try:
        translate = serial_translator()
        
    except rospy.ROSInterruptException:
        pass
