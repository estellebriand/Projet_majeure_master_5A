#!/usr/bin/env python


import rospy
import tf
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Twist, Point, PoseStamped, PointStamped, Pose2D
from nav_msgs.msg import Path, Odometry
from sensor_msgs.msg import LaserScan


from std_msgs.msg import Bool
from math import fabs, sqrt, atan2, pi, fmod

from projet.srv import localGoal 
from projet.srv import Path as PathToGoal 
from copy import copy, deepcopy



class LocalPlanner:
    """
        Move from one waypoint to another. Stop if an obstacle is detected
        pathPoses attribute contains a list of waypoints

        Suscribe (inputs):
            - laser scan
            - odom

        Publish (output)
            - robot velocity

        Service:        
            pathPoses attribute can be filled in with: 
                - goalService for a single waypoint
                - pathService for a full path
    """

    pathPoses = []
    currentTarget = Pose2D()
    curPose2D = Pose2D()
    isObstacle = False
    count = 0

    def __init__(self, K_linear, K_angular, Sat_linear, Sat_angular, Obstacle_range, Angle_to_allow_linear, Waypoint_error, Destination_error, Angle_error):
        # init params
        self.K_linear               = K_linear              # Proportionnal coefficient for linear velocity
        self.K_angular              = K_angular             # Proportionnal coefficient for angular velocity
        self.Sat_linear             = Sat_linear            # Max linear velocity
        self.Sat_angular            = Sat_angular           # Max angular velocity
        self.Obstacle_range         = Obstacle_range        # Distance below which we consider an obstacle
        self.Angle_to_allow_linear  = Angle_to_allow_linear # Below this value : angular control only. Above this value : angular and linear control together
        self.Waypoint_error         = Waypoint_error        # Euclidian distance error to a waypoint allowing to move to a new waypoint
        self.Destination_error      = Destination_error     # Euclidian distance error to the final waypoint below which we consider the position reached 
        self.Angle_error            = Angle_error           # Angular error below which we consider the final orientation reached

        # init ros node
        rospy.init_node('Planner', anonymous=False)

        # ------------------#
        #--- Subscriber ----#
        #-------------------#
        # get odometry
        rospy.Subscriber("/odom", Odometry, self.odomCallback)
        # get laser scan
        rospy.Subscriber("/scan", LaserScan, self.scanCallback)
        rospy.loginfo("Planner Subscribers initialized")

        # ------------------#
        # --- Publisher ----#
        # ------------------#
        # velocity command
        self.pub_velocity = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=100)
        rospy.loginfo("Planner publishers initialized")

        # ------------------#
        # ---- Service -----#
        # ------------------#
        self.goal_Srv = rospy.Service('/move_to/singleGoal', localGoal, self.goalService)
        self.path_Srv = rospy.Service('/move_to/pathGoal', PathToGoal, self.pathService)
        rospy.loginfo("Planner services initialized")

#******************************************************************************************
#*********************************   SUSCRIBERS CALLBACK   ********************************
#******************************************************************************************

    def odomCallback(self, odom):
        """
            Odometry callback
            Set curPose2D with current robot x y theta
        """

        #TODO for students : Fill in self.curPose2D (help : use euler_from_quaternion)
        euler = euler_from_quaternion([odom.pose.pose.orientation.x,odom.pose.pose.orientation.y,odom.pose.pose.orientation.z,odom.pose.pose.orientation.w]) 
        self.curPose2D.x = odom.pose.pose.position.x
        self.curPose2D.y = odom.pose.pose.position.y
        self.curPose2D.theta = euler[2]

        #rospy.loginfo("Odom => X: %.2f \t Y: %.2f \t theta: %.2f"  % (self.curPose2D.x, self.curPose2D.y, self.curPose2D.theta ) )

                
    def scanCallback(self, scan):
        """
            laser scan callback
            Detect (set isObstacle = true) if obstacle. If obstacle detected, log once every 100 call of this function
        """        
        #TODO for students : If an obstacle below self.Obstacle_range if detected, then self.isObstacle = True, False otherwise
        self.isObstacle = False
        ranges_list = scan.ranges
        self.count+=1

        for dist in ranges_list:
            if dist <= self.Obstacle_range:
                self.isObstacle = True
                 
                if self.count == 100:
                    self.count=0
                    rospy.loginfo("Obstacle detected")
        



#******************************************************************************************
#**************************************   SERVICES   **************************************
#******************************************************************************************

    def goalService(self, req):
        """
            ROS Service method 
            Add the pose in arg req to the path (self.pathPoses) if no obstacles are seen
            Return std_msgs/Bool at True
        """
        self.addPose2DToPath(req.goalPose2D, True)
        rospy.loginfo("Goal to x = %.2f    y = %.2f"  % (req.goalPose2D.x, req.goalPose2D.y) )
        fb = Bool()
        fb.data = not self.isObstacle
        return fb


    def pathService(self, req) :
        """
            # Clear the previous Path (self.pathPoses)
            # Try to add the Path received by the client to the Path (self.pathPoses) with a TF transform between the frame_id and /odom
            # Return std_msgs/Bool message with True if the "try" succeded, else (exception case) return False
        """           

        # request is the return of a fonction from testPathGenerator: return pm type Path() and it's a list of ps type PathStamped()
        # in the script "testPathGenerator", pm.poses.append( deepcopy(ps) ) and ps is :
        #ps.pose.position.x = 2.8
        #ps.pose.position.y = 2.8
        #ps.pose.orientation.w = 1.0

        rospy.loginfo('request received')
        fb = Bool()
        listener = tf.TransformListener() #creation of a listener type tf.TransformListener()


        try:
            now = rospy.Time(0)
            #Block until a transform is possible or it times out. 
            listener.waitForTransform(req.pathToGoal.header.frame_id, "/odom", now, rospy.Duration(2.0))
            
     
            for i in xrange( len(req.pathToGoal.poses) ) : 
                
                #Apply tranform on each PoseStamped with transformPose method out of tf.TransformListener()
                #listener.transform(ID_current_frame, path)
                listener.transformPose("odom",req.pathToGoal.poses[i])
                
                rospy.loginfo("# Pose %d : x = %.2f   y = %.2f" % (i, req.pathToGoal.poses[i].pose.position.x, req.pathToGoal.poses[i].pose.position.y) )

            del self.pathPoses[:]
            self.pathPoses = deepcopy( req.pathToGoal.poses )

            rospy.loginfo("### New path with %d poses" % int( len(self.pathPoses)  ) )
            fb.data = True


        except Exception as err:
            rospy.loginfo("%s",str(err))
            fb.data = False
            
        return fb


#******************************************************************************************
#**********************************   GOALS COMPUTATION   *********************************
#******************************************************************************************

    def shortestAngleDiff(self, th1, th2):
        """
            Returns the shortest angle between 2 angles in the trigonometric circle
        """        
        anglediff = fmod( (th1 - th2), 2*pi)

        if anglediff < 0.0:
            if fabs(anglediff) > (2*pi + anglediff) :
                anglediff = 2*pi + anglediff
        else:
            if anglediff > fabs(anglediff - 2*pi) :
                anglediff = anglediff - 2*pi

        return anglediff


    def addPose2DToPath(self, p, clear ) :
        """
            Add a pose p (type Pose2D) in the Path (self.pathPoses) to follow
            Argument clear (type bool) clear the existing Path (self.pathPoses) when set to true
        """   

        ps = PoseStamped()
        q = quaternion_from_euler(0.0, 0.0, p.theta)
        ps.header.frame_id = "odom"
        ps.header.stamp = rospy.Time.now()
        ps.header.seq = 0
        ps.pose.position.x = p.x
        ps.pose.position.y = p.y
        ps.pose.orientation.x = q[0]
        ps.pose.orientation.y = q[1]
        ps.pose.orientation.z = q[2]
        ps.pose.orientation.w = q[3]   

        if(clear) : 
            del self.pathPoses[:]
        self.pathPoses.append(ps)


    def computeDistAngle(self):
        """
            Compute the euclidian distance to the target and the angle between robot orientation and its target
            Return a tupple (distance, angle) with distance and angle to the target
        """           

        if len(self.pathPoses) > 0 :
            """
            Pose2D:
                float64 x
                float64 y
                float64 theta
            """
            currentTarget = self.pathPoses[0].pose.position
            #distCurTarget(norme):
            distCurTarget = sqrt((currentTarget.x-self.curPose2D.x)**2+(currentTarget.y-self.curPose2D.y)**2)

            #arc tangente
            theta = atan2(currentTarget.y-self.curPose2D.y,currentTarget.x-self.curPose2D.x)
            #angle
            angle = self.shortestAngleDiff(theta,self.curPose2D.theta)

            return (distCurTarget, angle)
        
        else:
            return (0, 0)



    def computeFinalOrientation(self):
        """
            Compute the final orientation based on the last waypoint orientation 
            Return an angle (float)
        """
        if len(self.pathPoses) > 0 :

            # pathPoses.pose.orientation --> quaternion to euler et prendre le theta
            # la derniere etape est de s'orienter comme a l'angle du dernier way point, dans le pathPoses
            euler = euler_from_quaternion([self.pathPoses[0].pose.orientation.x,self.pathPoses[0].pose.orientation.y,self.pathPoses[0].pose.orientation.z,self.pathPoses[0].pose.orientation.w]) 
            theta_goal =  euler[2]

            angle = self.shortestAngleDiff(theta_goal,self.curPose2D.theta)
            return angle       
        else:
            return 0



    def pathSequencer(self, dist, angle, finalOrientation):
        """
            Switch between the following sequences : "New Goal" <--> "Reach in progress" --> "Last Goal position Reached" --> "Last Goal pose (position + orientation) Reached"
            :return: One of the string: "New Goal", "Reach in progress",  "Last Goal position Reached", "Last Goal pose (position + orientation) Reached"
        """

        #SI on a atteint un way point mais qu'il en reste alors on continue avec une nouveau way point
        if(dist < self.Waypoint_error ) and len(self.pathPoses) > 1 :
            del self.pathPoses[0]
            #computeVelocity
            rospy.loginfo("# New goal : x=%f ; y=%f"  % ( self.pathPoses[0].pose.position.x, self.pathPoses[0].pose.position.y ) )
            return "New Goal"
        #SINON SI est a la position finale et qu'il ne reste plus de way point alors on verifie son orientation
        elif(dist < self.Destination_error ) and len(self.pathPoses) == 1 :
            if fabs(finalOrientation) >= self.Angle_error :
                state = "Last Goal position Reached"
            else:
                state = "Last Goal pose (position + orientation) Reached" #TODO for students : return string matching with the state

            rospy.loginfo("# %s : X = %.2f ; Y = %.2f "  % ( state, self.pathPoses[0].pose.position.x, self.pathPoses[0].pose.position.y ) )
            return state

        return "Reach in progress"



    def computeVelocity(self, dist, angle, goalState) :
        """
            Compute linear and angular velocity
            :param dist: Euclidian distance to the waypoint
            :param angle: Angle to the waypoint
            :param goalState: string giving the state out the pathSequencer method
            :rtype: geometry_msgs.msg/Twist
        """

        twist = Twist()
        
        #Apply gain and saturation (both ROSPARAM) to angle (as already done for linear velocity)
        twist.angular.z = min(angle * self.K_angular, self.Sat_angular) 

        if(fabs(angle) < self.Angle_to_allow_linear):
            #SI nouvelle postion ou qu'on se deplace, on verifie la presence d'un obstacle
            if "New Goal" == goalState or "Reach in progress" == goalState : #TODO for students : modify string matching with the state (help in pathSequencer docstring)
                if self.isObstacle == True:
                    twist.linear.x = 0
                else:
                    twist.linear.x = min(dist * self.K_linear, self.Sat_linear)   
        #SI on a fini le deplacemment et l'orientation alors on n'a pas de changement d'angle
        if "Last Goal pose (position + orientation) Reached" == goalState: #TODO for students : modify string matching with the state (help in pathSequencer docstring)
            twist.angular.z = 0

        return twist   
        


    def localPlanning(self):
        """
            Main loop (20Hz):
                1/ Call method to compute distance and angle to waypoint
                2/ If last waypoint (goal), Call method to compute final orientation 
                3/ Call method to manage the sequence and get the goalState
                4/ Depending on the case:
                    a/ Call method to compute new distance and angle to waypoint
                    b/ set angle to final orientation
                5/ Call method to compute velocity
                6/ Publish velocity
        """
        rate = rospy.Rate(20) # 20hz

        while not rospy.is_shutdown():

            (dist, angle) = self.computeDistAngle()
            if len( self.pathPoses ) == 1 :
                finalOrientation = self.computeFinalOrientation()
            else:
                finalOrientation = 0

            goalState = self.pathSequencer(dist, angle, finalOrientation)

            if "New Goal" == goalState:
                (dist, angle) = self.computeDistAngle()
            #Si on a atteint la position ou atteint la position et qu'on est bien oriente, on calcul l'angle final d'orientation, ca ne changera pas si on a deja la bonne orientation.
            elif "Last Goal position Reached" == goalState  or  "Last Goal pose (position + orientation) Reached" == goalState :  
                angle = finalOrientation


            twist = self.computeVelocity(dist, angle, goalState)
            self.pub_velocity.publish(twist)
            rate.sleep()



#******************************************************************************************
#***************************************   MAIN   *****************************************
#******************************************************************************************

if __name__ == '__main__':
    try:

        # ------------------#
        # --- ROS PARAM ----#
        # ------------------#
        K_LINEAR = rospy.get_param('~K_LINEAR', 1)
        K_ANGULAR = rospy.get_param('~K_ANGULAR', 4)
        SAT_LINEAR = rospy.get_param('~SAT_LINEAR', 2.0)
        SAT_ANGULAR = rospy.get_param('~SAT_ANGULAR', pi/2.0 )
        OBSTACLE_RANGE = rospy.get_param('~OBSTACLE_RANGE', 0.5)
        ANGLE_TO_ALLOW_LINEAR = rospy.get_param('~ANGLE_TO_ALLOW_LINEAR', 0.2)
        WAYPOINT_ERROR = rospy.get_param('~WAYPOINT_ERROR', 0.16)
        DESTINATION_ERROR = rospy.get_param('~DESTINATION_ERROR', 0.003)
        ANGLE_ERROR = rospy.get_param('~ANGLE_ERROR', 0.05)


        # ------------------#
        # Start LocalPlanner#
        # ------------------#        
        localPlanner = LocalPlanner(K_LINEAR, K_ANGULAR, SAT_LINEAR, SAT_ANGULAR, OBSTACLE_RANGE, ANGLE_TO_ALLOW_LINEAR, WAYPOINT_ERROR, DESTINATION_ERROR, ANGLE_ERROR)

        localPlanner.localPlanning()

        rospy.spin()

    except rospy.ROSInterruptException:
        pass
