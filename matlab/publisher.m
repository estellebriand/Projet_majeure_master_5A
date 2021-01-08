% Publisher
%% Init
%to share variable for calling callback function
global pos
global orient
%set python environment
pe = pyenv('Version','2.7');
pe.Version

%start roscore
rosinit

chatterpub = rospublisher('/chatter', 'std_msgs/String')
pause(2) % Wait to ensure publisher is registered

%Define a subscriber for the /chatter topic. exampleHelperROSChatterCallback is called when a new message is received and displays the string content in the message.
chattersub = rossubscriber('/chatter', @exampleHelperROSChatterCallback)

%% Publish
%Create and populate a ROS message to send to the /chatter topic.
chattermsg = rosmessage(chatterpub);
chattermsg.Data = 'hello world'
send(chatterpub,chattermsg)

pause(2)
rostopic list