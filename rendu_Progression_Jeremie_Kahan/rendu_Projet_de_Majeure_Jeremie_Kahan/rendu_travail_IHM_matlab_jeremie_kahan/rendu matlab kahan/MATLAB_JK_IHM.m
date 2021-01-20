% JK_IHM
clear variables;
clc;
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
waypoints = [];