%% test ROS matlab
%set python environment
pe = pyenv('Version','2.7');
pe.Version

%start roscore
rosinit
%to connect to a network
%rosinit(192.168.1.1,'NodeHost','192.168.1.100')
%%master_host,"NodeHost",your IP)

%start node
exampleHelperROSCreateSampleNetwork
fprintf("\tnode launched\n")
rosnode list
fprintf("")
rosnode info /node_1
fprintf("\ttopics\n")
rostopic list
fprintf("")
rostopic info /pose
fprintf("\nrosmgs show\n")
rosmsg show geometry_msgs/Twist
rosshutdown