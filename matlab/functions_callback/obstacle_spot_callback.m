function obstacle_spot_callback(obstacles,data)
%OBSTACLE_SPOT_CALLBACK Summary of this function goes here
%   Detailed explanation goes here
global robot;
global test_variable_Estelle;
global app;

list_obstacles = data.Data;
position = split(list_obstacles,",");
pos = [split(position(1)), split(position(2)),split(position(3)),split(position(4))];
map_obstacles = containers.Map([pos(1,1),pos(1,2),pos(1,3),pos(1,4)],[pos(2,1),pos(2,2),pos(2,3),pos(2,4)]);
keys(map_obstacles);
robot.Obstacle = robot.Obstacle.update(map_obstacles);
test_variable_Estelle = robot.Obstacle.Front;
func_IHM(app);
% if robot.Obstacle.Front == "True"
%     mylamps(1).Color = 'red';
% else mylamps(1).Color = 'g';
% end
% 
% if robot.Obstacle.Back == "True"
%     mylamps(2).Color = 'red';
% else mylamps(2).Color = 'g';
% end
% 
% if robot.Obstacle.Left == "True"
%     mylamps(3).Color = 'red';
% else mylamps(3).Color = 'g';
% end
% 
% if robot.Obstacle.Right == "True"
%     mylamps(4).Color = 'red';
% else mylamps(4).Color = 'g';
% end

end

