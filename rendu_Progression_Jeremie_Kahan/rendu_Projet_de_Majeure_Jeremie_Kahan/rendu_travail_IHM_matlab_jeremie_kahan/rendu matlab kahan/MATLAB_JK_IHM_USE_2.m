clc;

map = occupancyMap(map_matrix);
planner = plannerAStarGrid(map);
start = [500 2500];
goal = [4500 2500];
path = plan(planner,start,goal);
disp(path);
show(planner);

figure()
plot(path)