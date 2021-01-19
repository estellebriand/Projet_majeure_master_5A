function vision_callback(vision,data)
%VISION_CALLBACK Summary of this function goes here
%   Detailed explanation goes here
global robot
global app

liste = split(data.Data);

robot.Vision = data.Data;
func_IHM(app);
end

