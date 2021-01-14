% JK_IHM
%clear variables;
%clc;
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



% Tests
for idx = 1:10
    pose = pose + [0; 0; pi/8];
    viz(pose)
    pause(0.25)
end 

%% Estelle :
% Variable que tu veux faire passer
test_variable_Estelle = "Hello World I'm Estelle!";
% Nom du Matlab App associé
app = APP_JK_HIL_IHM_v10_0_estelle_variable_test;
% Appel de la fonction "func_IHM" créée dans Matlab App
results = func_IHM(app);