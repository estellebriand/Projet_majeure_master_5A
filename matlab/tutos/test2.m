%% Publisher / Subscriber
%to share variable for calling callback function
global pos
global orient
%set python environment
pe = pyenv('Version','2.7');
pe.Version

%start roscore
rosinit
%start node
exampleHelperROSCreateSampleNetwork

laser = rossubscriber('/scan');
pause(2)
scandata = receive(laser,10)
figure
plot(scandata,'MaximumRange',7)

robotpose = rossubscriber('/pose',@exampleHelperROSPoseCallback)