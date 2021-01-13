#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String, Empty

class Subscrib():
    def __init__(self):
        
        rospy.init_node('listener', anonymous=True)

        pub = rospy.Subscriber('/talker_matlab', String, self.printer)
        rospy.loginfo("Node [listener] started")
        
        self.add_two_ints_client(1,2)
    def printer(self,data):
        print data
    
    def add_two_ints_client(self,x,y):
        rospy.wait_for_service('/test')

        fonction = rospy.ServiceProxy('/test', Empty)
        rep = fonction()
        print "DONE"


if __name__ == '__main__':
    try:
        Subscrib()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

