function ultrason_callback(ultrason,data)
%ULTRASON_CALLBACK Summary of this function goes here
%   Detailed explanation goes here
global robot
global app
robot.Ultrason = double(data.Data);
func_IHM(app);
end

