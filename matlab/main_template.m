%% Init

% Add path to folders
addpath(genpath("classes")) % folder with all classes 
addpath(genpath("functions_callback")) % folder with all function callback for subscriber

% to share variable for calling callback function
global robot ; % Robot object
global mylamps;
robot = robot_class("Test");

%set python environment
pe = pyenv('Version','2.7');
%visual
fig = uifigure;
mylamp1 = uilamp(fig);
mylamp1.Position = [250 250 20 20];
mylamp2 = uilamp(fig);
mylamp2.Position = [250 050 20 20];
mylamp3 = uilamp(fig);
mylamp3.Position = [150 150 20 20];
mylamp4 = uilamp(fig);
mylamp4.Position = [350 150 20 20];
mylamps = [mylamp1,mylamp2,mylamp3,mylamp4];
%start roscore
%rosinit("192.168.1.54")
rostopic list

%% Publishers
%publisher = rospublisher('/publisher_topic', 'msg_type');

%% Subscribers
laserscan = rossubscriber('/scan', 'sensor_msgs/LaserScan', @scan_callback);
obstacles = rossubscriber('/obstacle_spot', 'std_msgs/String', @obstacle_spot_callback);

fprintf("Node [main_template_matlab] started")
pause(2) 


% Check the robot information 
robot.Obstacle.Front;

for i = 1:10
	fprintf("\nY a-t-il un obstacle derriere ?: %s\n", robot.is_obstacle('derriere'))
	pause(0.5) 

end

% create and pub the msg
% msg = rosmessage(msg_type);
% msg.Data = 'talker matlab';
% send(publisher,msg);
% pause(2);


%% call service /add_two_ints
%client = rossvcclient('/add_two_ints')
%req = rosmessage(client)
%req.a = 1
%req.b = 2
%resp = call(client,req,'Timeout',3);

%exampleHelperROSCreateSampleNetwork
%testserver = rossvcserver('/test', 'std_srvs/Empty', @exampleHelperROSEmptyCallback)
%% Rosbag
%device = rosdevice('192.168.1.54','ros-ubuntu','projet2020')
%getFile(device,'~/Bureau/projet_ws/bagfiles/bagfile.bag')
%bag = rosbag('bagfile.bag')
 
% Display a list of the topics and message types in the bag file
%  
% Get just the topic we are interested in
%bagselect = select(bag,'Topic','turtle1/pose');
