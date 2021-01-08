%% Init
%to share variable for calling callback function

%set python environment
pe = pyenv('Version','2.7');
pe.Version

%start roscore
rosinit("192.168.1.54")
rostopic list
getFile(d,'~/Bureau/projet_ws/bagfiles/bagfile.bag')
bag = rosbag('bagfile.bag')
 
% Display a list of the topics and message types in the bag file
bag.AvailableTopics
 
% Since the messages on topic turtle1/pose are of type Twist,
% let's see some of the attributes of the Twist message
msg_pose = rosmessage('turtlesim/Pose')
showdetails(msg_pose)
 
% Get just the topic we are interested in
bagselect = select(bag,'Topic','turtle1/pose');
 
% Create a time series object based on the fields of the turtlesim/Pose
% message we are interested in
ts = timeseries(bagselect,'X','Y','Theta','LinearVelocity','AngularVelocity');