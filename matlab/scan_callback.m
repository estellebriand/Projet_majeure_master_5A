function scan_callback(laserscan,data)
%SCAN_CALLBACK Summary of this function goes here
%   Detailed explanation goes here
global scan 
scan = data.Ranges;
t = 1:360;
plot(scan,t);
end

