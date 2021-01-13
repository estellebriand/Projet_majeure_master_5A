function obstacle_spot_callback(obstacles,data)
%OBSTACLE_SPOT_CALLBACK Summary of this function goes here
%   Detailed explanation goes here
global robot;

list_obstacles = data.Data;
position = split(list_obstacles,",");
pos = [split(position(1)), split(position(2)),split(position(3)),split(position(4))];
map_obstacles = containers.Map([pos(1,1),pos(1,2),pos(1,3),pos(1,4)],[pos(2,1),pos(2,2),pos(2,3),pos(2,4)]);
keys(map_obstacles);
obj_obstacle = obstacle_class(map_obstacles);
robot.Obstacle = obj_obstacle;
end

