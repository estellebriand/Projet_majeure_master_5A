#!/usr/bin/env python
from projet.srv import AddTwoInts,AddTwoIntsResponse
import rospy


class add_two_ints_server():
    def __init__(self):
        rospy.init_node('add_two_ints_server')
        s = rospy.Service('add_two_ints', AddTwoInts, self.handle_add_two_ints)
        print("Ready to add two ints. ")
    
    def handle_add_two_ints(req):
        print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
        return AddTwoIntsResponse(req.a + req.b)

if __name__ == "__main__":
    add_two_ints_server()
    rospy.spin()
