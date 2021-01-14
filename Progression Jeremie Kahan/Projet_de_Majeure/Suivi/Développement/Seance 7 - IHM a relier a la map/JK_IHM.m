% JK_IHM
clc;
clear variables;
% Creation de la base de la carte (son fond), et sa configuration
% https://fr.mathworks.com/help/nav/ref/occupancymap.html
% CHOICES : 30 meters wide & 30 meters long & resolution : 1 mm per cell 
map_matrix = eye(30,30);

jk_map = occupancyMap(map_matrix);

% Chargement de la carte
viz = Visualizer2D;
viz.showTrajectory = false;
load jk_map
viz.mapName = 'jk_map';
pose = [3; 4; 0];
viz(pose)



% Tests
for idx = 1:10
    pose = pose + [0; 0; pi/8];
    viz(pose)
    pause(0.25)
end