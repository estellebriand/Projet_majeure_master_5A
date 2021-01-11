%% Init
%to share variable for calling callback function
global variable
%set python environment
pe = pyenv('Version','2.7');
% pe.Version

%start roscore
%rosinit("192.168.1.54")
rostopic list

%% subscribe /chatter topic
% chatter_callback will update the global variable variable with
% data.Data 
%chatter = rossubscriber('/chatter', @chatter_callback);
%pause(2) 
% we print the global variable
%fprintf("%s",variable)

%% call service /add_two_ints
client = rossvcclient('/add_two_ints')
req = rosmessage(client)
req.a = 1
req.b = 2
resp = call(client,req,'Timeout',3);
%% Rosbag
%device = rosdevice('192.168.1.54','ros-ubuntu','projet2020')
%getFile(device,'~/Bureau/projet_ws/bagfiles/bagfile.bag')
%bag = rosbag('bagfile.bag')
 
% Display a list of the topics and message types in the bag file
%  
% Get just the topic we are interested in
%bagselect = select(bag,'Topic','turtle1/pose');
