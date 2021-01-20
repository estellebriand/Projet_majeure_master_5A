# Import the required libraries...
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import Int32
from moveit_commander.conversions import pose_to_list

#stop forward turn_left turn_right bras_haut_pince_ouverte bras_haut_pince_fermee bras_bas_pince_ouverte bras_bas_pince_fermee


class moveit_test_named_target():
# While the node is ON, move predefined targets to another : "straight" -> "right" -> "left" -> ...
# Use the method set_named_target()    
    def __init__(self):
       # DEFINIR UN SUBSCRIBER QUI VA RECEVOIR L ORDRE LEFT/RIGHT/STRAIGHT ET QUI VA DECLENCHER LA POSITION
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('HIL_position_listener', anonymous=True)
	self.robot = moveit_commander.RobotCommander()
	self.scene = moveit_commander.PlanningSceneInterface()
        self.bras = moveit_commander.MoveGroupCommander("HIL_group")
	self.robot = moveit_commander.RobotCommander()
	self.scene = moveit_commander.PlanningSceneInterface()
	self.sub_pos = rospy.Subscriber("/command", Int32, self.position_choice_callback)



    def position_choice_callback(self, position_choice_data):
        if position_choice_data.data == 0:
            self.go_to_position_stop()
            rospy.loginfo("Consigne : go to position stop")
        elif position_choice_data.data == 1:
            self.go_to_position_forward()
            rospy.loginfo("Consigne : go to position forward")
        elif position_choice_data.data == 2:
            self.go_to_position_turn_left()
            rospy.loginfo("Consigne : go to position turn_left")
        elif position_choice_data.data == 3:
            self.go_to_position_turn_right()
            rospy.loginfo("Consigne : go to position turn_right")
        elif position_choice_data.data == 4:
            self.go_to_position_bras_haut_pince_ouverte()
            rospy.loginfo("Consigne : go to position bras_haut_pince_ouverte")
        elif position_choice_data.data == 5:
            self.go_to_position_bras_haut_pince_fermee()
            rospy.loginfo("Consigne : go to position bras_haut_pince_fermee")
        elif position_choice_data.data == 6:
            self.go_to_position_bras_bas_pince_ouverte()
            rospy.loginfo("Consigne : go to position bras_bas_pince_ouverte")
        elif position_choice_data.data == 7:
            self.go_to_position_bras_bas_pince_fermee()
            rospy.loginfo("Consigne : go to position bras_bas_pince_fermee")
        else:
            rospy.loginfo("Erreur de consigne")





    def go_to_position_stop(self):
	rospy.sleep(2)
	p = geometry_msgs.msg.PoseStamped()
	p.header.frame_id = "robot/chassis"
	p.pose.position.x = 0.0
	p.pose.position.y = 0.0
	p.pose.position.z = 0.4
	self.scene.add_sphere("ball", p, radius=0.1)
	rospy.sleep(2)
	self.scene.remove_world_object("ball")

    def go_to_position_forward(self):
	rospy.sleep(2)
	p = geometry_msgs.msg.PoseStamped()
	p.header.frame_id = "robot/chassis"
	p.pose.position.x = 1.0
	p.pose.position.y = 0.0
	p.pose.position.z = 0.1
	self.scene.add_sphere("ball", p, radius=0.1)
	rospy.sleep(2)
	self.scene.remove_world_object("ball")
	


    def go_to_position_turn_left(self):
	rospy.sleep(2)
	p = geometry_msgs.msg.PoseStamped()
	p.header.frame_id = "robot/chassis"
	p.pose.position.x = 0.0
	p.pose.position.y = 0.6
	p.pose.position.z = 0.1
	self.scene.add_sphere("ball", p, radius=0.1)
	rospy.sleep(2)
	self.scene.remove_world_object("ball")

    def go_to_position_turn_right(self):
	rospy.sleep(2)
	p = geometry_msgs.msg.PoseStamped()
	p.header.frame_id = "robot/chassis"
	p.pose.position.x = 0.0
	p.pose.position.y = -0.5
	p.pose.position.z = 0.1
	self.scene.add_sphere("ball", p, radius=0.1)
	rospy.sleep(2)
	self.scene.remove_world_object("ball")

    def go_to_position_bras_haut_pince_ouverte(self):
        self.bras.set_named_target("bras_haut_pince_ouverte")
        self.bras.go()

    def go_to_position_bras_haut_pince_fermee(self):
        self.bras.set_named_target("bras_haut_pince_fermee")
        self.bras.go()

    def go_to_position_bras_bas_pince_ouverte(self):
        self.bras.set_named_target("bras_bas_pince_ouverte")
        self.bras.go()    

    def go_to_position_bras_bas_pince_fermee(self):
        self.bras.set_named_target("bras_bas_pince_fermee")
        self.bras.go()




if __name__=='__main__':
  try:
    moveit_test_named_target()
    rate = rospy.Rate(1)
    rate.sleep()
    rospy.spin()
  except rospy.ROSInterruptException:
    pass
