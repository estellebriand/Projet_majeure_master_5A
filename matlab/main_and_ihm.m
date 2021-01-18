% main_IHM
%clear variables;
%clc;

%% Init
%add path
addpath(genpath("classes")); % folder with all classes 
addpath(genpath("functions_callback")); % folder with all function callback for subscriber
addpath(genpath("mobile-robotics-simulation-toolbox"));

% global varables
global robot;
global test_variable_Estelle; % Variable pour ihm
global app; % Nom du Matlab App associé

%set python environment
pe = pyenv('Version','2.7');
robot = robot_class("test","192.168.43.209");
%% IHM
startMobileRoboticsSimulationToolbox 
test_variable_Estelle = robot.Obstacle.Left;

% Creation de la base de la carte (son fond), et sa configuration
% https://fr.mathworks.com/help/nav/ref/occupancymap.html
% CHOICES : 30 meters wide & 30 meters long & resolution : 1 mm per cell 
map_matrix = zeros(5000,5000);
step_count = 0;
step_list = [];
x1_coord_list = [];
y1_coord_list = [];
x2_coord_list = [];
y2_coord_list = [];
margin_error_list = [];
x_operations_list = {};
y_operations_list = {};
step_operations_list = [];

jk_map = occupancyMap(map_matrix);

% Chargement de la carte
viz = Visualizer2D;
viz.showTrajectory = false;
load jk_map
viz.mapName = 'jk_map';
pose = [3; 4; 0];
viz(pose)

app = APP_JK_HIL_IHM_v10_0_estelle_variable_test;
%% ROS
%simu = RobotSimulator
path = [1,1 ; 2,10 ; 3, 12345; 4,987 ; 5,1222];


rosshutdown;
rosinit(robot.Ip_address) %start roscore
rostopic list

pause(10) % wait for ihm 
% Publishers
%command_vel_pub = rospublisher('/matlab/cmd_vel', std_msgs/Twist);
% Subscribers
laserscan = rossubscriber('/scan', 'sensor_msgs/LaserScan', @scan_callback);
obstacles = rossubscriber('/obstacle_spot', 'std_msgs/String', @obstacle_spot_callback);
rossubscriber('/imu', 'std_msgs/String', @imu_callback);

fprintf("Node [main_template_matlab] started")
% create and pub the msg
%msg = rosmessage(std_msgs/Twist);
% msg.Data = 'talker matlab';
%send(command_vel_pub,msg);
pause(2) 

%% Estelle :
%test_variable_Estelle = "Hello World I'm Estelle!";

% Appel de la fonction "func_IHM" créée dans Matlab App
% results = func_IHM(app);