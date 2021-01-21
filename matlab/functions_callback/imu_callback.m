function imu_callback(event,data)
%IMU_CALLBACK Summary of this function goes here
%   Detailed explanation goes here
global robot;
global app;
angular = split(data.Data);

%robot.Orientation = data.Data;

robot.Orientation.Angular.X = str2double(angular(2));
robot.Orientation.Angular.Y = str2double(angular(4));

z = 180 + str2double(angular(6));
robot.Orientation.Angular.Z = z;

end

