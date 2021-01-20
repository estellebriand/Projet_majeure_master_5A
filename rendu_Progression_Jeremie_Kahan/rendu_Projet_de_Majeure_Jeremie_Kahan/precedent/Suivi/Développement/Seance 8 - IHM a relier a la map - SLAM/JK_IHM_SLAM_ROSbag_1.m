% Toolbox ROS => 'rosbag' => SLAM App => 'Automated_occupancy_lidar_map' => IHM
clc;
clear variables;
% Verifier la version Python installee, si erreur, installer la version 2.7
disp("Lancement du systeme de communication ROS en cours");
pe = pyenv;
pe.Version

% Initialiser ROS avec un ROScore si il n'est pas deja lance...
rosshutdown
rosinit


load slamLidarScans.mat



% Manipulation des ROSbag
%bag = rosbag(filename)

